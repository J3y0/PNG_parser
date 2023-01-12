import sys

class PNGImage(object):

    def __init__(self, path):
        self.path = path
        self.height = 0
        self.width = 0
        self.crc = 0
        
    def is_png(self):
        """
        Check the magic bytes of the file
        """
        with open(self.path, "rb") as f:
            beginning = f.read(8)
            png_magic_bytes = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
            return list(beginning) == list(png_magic_bytes)

    def parse_header(self):
        pass

    def parse_chunk(self):
        pass

    def parse(self):
        self.parse_header()
        self.parse_chunk()

    def __repr__(self):
        pass

def print_help():
    print("Parse the different chunks of a PNG image")
    print()
    print("Usage:")
    print("  python3 ./parser.py [file_path]")

if __name__ == "__main__":
    image_path = ""
    if len(sys.argv) != 2:
        print_help()
    else:
        image_path = sys.argv[1]
    my_png = PNGImage(image_path)
    print(my_png.is_png())
