import pyperclip
from time import sleep
sleep(1)
s = pyperclip.paste()
pyperclip.copy(s)
print(type(s))
print(s)