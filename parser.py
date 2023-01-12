import sys

class PNGImage(object):

    def __init__(self, path):
        self.path = path
        self.height = 0
        self.width = 0
        self.crc = 0
        
    def is_png(self):
        pass

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
    pass

if __name__ == "__main__":
    image_path = ""
    if len(sys.argv) != 1:
        print_help()
    else:
        image_path = sys.argv[1]
    my_png = PNGImage(image_path)
    my_png.parse()
