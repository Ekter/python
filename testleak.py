from Crypto.Cipher import AES


with open("data2.txt", "r", encoding="utf-8") as f:
    data: str = f.readlines()

print(data)

d = ""
for i in data:
    d+=chr(int(i.removesuffix("\n"), base=2))


key = d.replace("\x00", "").encode("utf-8")
print( d.replace("\x00", ""))
cipher = AES.new(key, AES.MODE_ECB)


with open("data.txt", "r", encoding="utf-8") as f:
    data: str = f.readlines()

print("\n", data)
a = ""
for i in data:
# for i in data[1::3]:
        # try:
            # print(chr(int(i.removesuffix("\n")[::-1], base=2)), end="")

    # curr = chr(int(i.removesuffix("\n")[:8], base=2)) + chr(int(i.removesuffix("\n")[8:], base=2))

    a+=f"{i.strip()}"


    # print(chr(curr), end="")
            # print(chr(int(i.removesuffix("\n")[8::-1], base=2)), end="")
        # except UnicodeEncodeError:
        #     print(f"<{i.removesuffix("\n")}>", end="")
        #     continue
    # print()

print(a)

# convert r to bytearray
br = bytearray()

for i in range(0, len(a), 8):
    br.append(int(a[i:i+8], base=2))

print(br)

plaintext = cipher.decrypt(br)
print(plaintext.decode("utf-8"))
