import binascii
import entropy
import sys


class PNGImage(object):

    def __init__(self, path):
        self.path = path
        self.current_offset = 0

    def parse_header(self):
        """
        Parse the header of the PNG file
        """
        with open(self.path, "rb") as f:
            f.seek(8)
            # Length of the following chunk data
            chunk_data_length = int(f.read(4).hex(), 16)

            # Chunk type
            chunk_type = f.read(4)

            # chunk_data
            chunk_data = f.read(chunk_data_length)

            # read CRC
            crc = "0x" + f.read(4).hex()

            # Computed CRC and entropy
            crc_computed = "0x" + hex(binascii.crc32(chunk_type + chunk_data))
            entpy = round(entropy.entropy(entropy.create_dict(chunk_data)), 2)
            
            self.current_offset = 8 + 4 + 4 + chunk_data_length + 4

            chunk_type = chunk_type.decode()
            print(chunk_type, chunk_data_length, crc, crc_computed, entpy, sep=", ")
            return chunk_type


    def parse_chunk(self, offset):
        """
        Parse a chunk of the PNG file
        """
        with open(self.path, "rb") as f:
            f.seek(offset)
            # Length of the following chunk data
            chunk_data_length = int(f.read(4).hex(), 16)

            # Chunk type
            chunk_type = f.read(4)

            # Chunk data
            chunk_data = f.read(chunk_data_length)

            # Read CRC
            crc = "0x" + f.read(4).hex()
            
            # Computed CRC and entropy
            crc_computed = "0x" + hex(binascii.crc32(chunk_type + chunk_data))
            entpy = round(entropy.entropy(entropy.create_dict(chunk_data)), 2)
            
            self.current_offset = offset + 4 + 4 + chunk_data_length + 4
            
            chunk_type = chunk_type.decode()
            print(chunk_type, chunk_data_length, crc, crc_computed, entpy, sep=", ")
            return chunk_type

    def parse(self):
        """
        Parse the entire PNG file
        The function prints chunks information as a CSV output:
            type, size, CRC, CRC_ref, entropy
        """
        print("type, size, CRC, CRC_ref, entropy")
        parsed_type = self.parse_header()
        while parsed_type != "IEND":
            parsed_type = self.parse_chunk(self.current_offset)


def print_help():
    """
    Print the help message
    """
    print("Parse the different chunks of a PNG image")
    print()
    print("Usage:")
    print("  python3 ./parser.py [file_path]")

def is_png(path):
    """
    Check if the file pointed out by the path is a PNG
    """
    with open(path, "rb") as f:
        beginning = f.read(8)
        png_magic_bytes = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
        return list(beginning) == list(png_magic_bytes)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_help()
        sys.exit(0)

    image_path = sys.argv[1]
    if not is_png(image_path):
        print("Error, not a PNG file")
        sys.exit(0)

    my_png = PNGImage(image_path)
    my_png.parse()
