#!/usr/bin/env python3

import sys
import base64


print(bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"))

print(bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"))

from tkinter import Tk

r = Tk()
r.withdraw()
r.clipboard_clear()

if len(sys.argv) < 2:
    data = sys.stdin.read()
else:
    data = ' '.join(sys.argv[1:])

r.clipboard_append(data)
print("ezf")
if sys.platform != 'win32':
    if len(sys.argv) > 1:
        input('Data was copied into clipboard. Paste and press ENTER to exit...')
        print("aqfsd")
    else:
        print('Data was copied into clipboard. Paste, then close popup to exit...')
        r.deiconify()
        r.mainloop()
else:
    r.destroy()
