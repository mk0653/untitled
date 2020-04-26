import struct
import numpy as np
import os
import sys
from PIL import Image

assert(len(sys.argv) == 2)
filename = sys.argv[1]

RECORD_SIZE = 8199
i = 0
print("Reading {}".format(filename))
with open(filename, 'rb') as f:
    while True:
        s = f.read(RECORD_SIZE)
        if s is None or len(s) < RECORD_SIZE:
            break
        r = struct.unpack(">HH8sIBBBBHHHHBB30x8128s11x", s)
        img = Image.frombytes('F', (128, 127), r[14], 'bit', (4, 0))
        img = img.convert('L')
        img = img.point(lambda x: 255 - (x << 4))
        i = i + 1
        dirname = b'\x1b$B' + r[1].to_bytes(2, 'big') + b'\x1b(B'
        dirname = dirname.decode("iso-2022-jp")
        try:
            os.makedirs(f"extract/{dirname}")
        except:
            pass
        imagefile = f"extract/{dirname}/{filename}_{i:0>6}.png"
        print(imagefile)
        img.save(imagefile)