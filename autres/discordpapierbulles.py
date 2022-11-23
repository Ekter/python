import random
import pyperclip

def pop(content="pop"):
    return f"||{content}|| "

s=""
while len(s)<1900:
    s += pop("pop") if random.randint(0, 37) else pop("opo")

pyperclip.copy(s)
print(s)
print("opo" in s)