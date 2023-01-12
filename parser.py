import binascii
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

            crc_computed = "0x" + hex(binascii.crc32(chunk_type + chunk_data))
            entropy = 0
            self.current_offset = 8 + 4 + 4 + chunk_data_length + 4

            chunk_type = chunk_type.decode()
            print(chunk_type, chunk_data_length, crc, crc_computed, entropy, sep=",")
            return chunk_type


    def parse_chunk(self, offset):
        """
        Parse a chunk of the PNG file
        """
        with open(self.path, "rb") as f:
            f.seek(offset)
            chunk_data_length = int(f.read(4).hex(), 16)
            chunk_type = f.read(4)

            chunk_data = f.read(chunk_data_length)
            crc = "0x" + f.read(4).hex()

            crc_computed = "0x" + hex(binascii.crc32(chunk_type + chunk_data))
            entropy = 0
            self.current_offset = offset + 4 + 4 + chunk_data_length + 4
            
            chunk_type = chunk_type.decode()
            print(chunk_type, chunk_data_length, crc, crc_computed, entropy, sep=",")
            return chunk_type

    def parse(self):
        print("type, size, CRC, CRC_ref, entropy")
        parsed_type = self.parse_header()
        while parsed_type != "IEND":
            parsed_type = self.parse_chunk(self.current_offset)


def print_help():
    print("Parse the different chunks of a PNG image")
    print()
    print("Usage:")
    print("  python3 ./parser.py [file_path]")

def is_png(path):
    """
    Check the magic bytes of the file
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
