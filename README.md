# PNG PARSER

This repository aims at parsing a PNG file. More precisely, the code 
goes through each chunk of the PNG and lists some characteristics 
according to the following pattern:

`type, size, CRC, CRC_ref, entropy`

That is, respectively the chunk_type, the length of the chunk data, 
the CRC , the CRC computed and the entropy of the chunk data.


# USAGE

To use the code, you must have python already installed. Then, you
have to specify the path of your file:

```bash
python3 ./parser.py [file-path]
```

# OUTPUT EXAMPLE

```bash
[ png_parser ] on  main & python3 ./parser.py ./logo.png                        
type, size, CRC, CRC_ref, entropy
IHDR, 13, 0x23232059, 0x0x23232059, 1.3
IDAT, 8192, 0xb7530128, 0x0xb7530128, 5.43
IDAT, 8192, 0xfcf12fa1, 0x0xfcf12fa1, 5.52
IDAT, 8192, 0x9a3a8c27, 0x0x9a3a8c27, 5.52
IDAT, 8192, 0xc77c536d, 0x0xc77c536d, 5.53
IDAT, 8192, 0xbdabd395, 0x0xbdabd395, 5.52
IDAT, 8192, 0xaaae2f57, 0x0xaaae2f57, 5.52 
```

# BIBLIOGRAPHY

[Useful documentation](http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html)
