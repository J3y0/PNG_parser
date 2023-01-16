import binascii
import entropy
import sys

MAGIC_BYTES_LENGTH = 8
CHUNK_LENGTH_BYTES_LENGTH = 4
CHUNK_TYPE_BYTES_LENGTH = 4
CRC_BYTES_LENGTH = 4

class PNGImage(object):

    def __init__(self, path):
        self.path = path
        self._current_offset = 0
        self._current_chunk_type = ""

    def _parse_header(self) -> None:
        """
        Parse the header of the PNG file
        """
        with open(self.path, "rb") as f:
            f.seek(MAGIC_BYTES_LENGTH)
            # Length of the following chunk data
            # use struct package
            chunk_data_length = int(f.read(CHUNK_LENGTH_BYTES_LENGTH).hex(), 16)

            # Chunk type
            chunk_type = f.read(CHUNK_TYPE_BYTES_LENGTH)

            # chunk_data
            chunk_data = f.read(chunk_data_length)

            # read CRC
            crc = "0x" + f.read(CRC_BYTES_LENGTH).hex()

            # Computed CRC and entropy
            crc_computed = hex(binascii.crc32(chunk_type + chunk_data))
            entpy = round(entropy.entropy(entropy.create_dict(chunk_data)), 2)
            
            self._current_offset = MAGIC_BYTES_LENGTH + CHUNK_LENGTH_BYTES_LENGTH + CHUNK_TYPE_BYTES_LENGTH + chunk_data_length + CRC_BYTES_LENGTH
            self._current_chunk_type = chunk_type.decode()

            print(self._current_chunk_type, chunk_data_length, crc, crc_computed, entpy, sep=", ")


    def _parse_chunk(self) -> None:
        """
        Parse a chunk of the PNG file
        """
        with open(self.path, "rb") as f:
            f.seek(self._current_offset)
            # Length of the following chunk data
            chunk_data_length = int(f.read(CHUNK_LENGTH_BYTES_LENGTH).hex(), 16)

            # Chunk type
            chunk_type = f.read(CHUNK_TYPE_BYTES_LENGTH)

            # Chunk data
            chunk_data = f.read(chunk_data_length)

            # Read CRC
            crc = "0x" + f.read(CRC_BYTES_LENGTH).hex()
            
            # Computed CRC and entropy
            crc_computed = hex(binascii.crc32(chunk_type + chunk_data))
            entpy = round(entropy.entropy(entropy.create_dict(chunk_data)), 2)
            
            self._current_offset = self._current_offset + CHUNK_LENGTH_BYTES_LENGTH + CHUNK_TYPE_BYTES_LENGTH + chunk_data_length + CRC_BYTES_LENGTH
            self._current_chunk_type = chunk_type.decode()
            
            print(self._current_chunk_type, chunk_data_length, crc, crc_computed, entpy, sep=", ")

    def parse(self) -> None:
        """
        Parse the entire PNG file
        The function prints chunks information as a CSV output:
            type, size, CRC, CRC_ref, entropy
        """
        print("type, size, CRC, CRC_ref, entropy")
        self._parse_header()
        while self._current_chunk_type != "IEND":
            self._parse_chunk()


def print_help() -> None:
    """
    Print the help message
    """
    print("Parse the different chunks of a PNG image")
    print()
    print("Usage:")
    print("  python3 ./parser.py [file_path]")

def is_png(path: str) -> bool:
    """
    Check if the file pointed out by the path is a PNG
    """
    with open(path, "rb") as f:
        beginning = f.read(MAGIC_BYTES_LENGTH)
        png_magic_bytes = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
        return list(beginning) == list(png_magic_bytes)

if __name__ == "__main__":
    # use argparse
    if len(sys.argv) != 2:
        print_help()
        # use main function returning an int
        sys.exit(0)

    image_path = sys.argv[1]
    if not is_png(image_path):
        print("Error, not a PNG file")
        sys.exit(0)

    my_png = PNGImage(image_path)
    my_png.parse()
