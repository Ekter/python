def sol(pl:str):
    cmap = lambda c: "".join(str(int(func(*[int(x) for x in format(ord(c) - ord('a'), '05b')]))) for func in [
        lambda x2, x3, x4, x5, x6: (not x5 and ((x2 and not x4) or not x3)) or (not x2 and (x4 or x5)) or (not x3 and x4 and x6),
        lambda x2, x3, x4, x5, x6: (x2 and not x3 and not x4) or (not x2 and x3 and not x4 and not x5) or (not x2 and x3 and x5 and x6) or (not x2 and not x3 and x4 and x5) or (not x3 and x4 and x5 and not x6) or (not x3 and not x5 and x6),
        lambda x2, x3, x4, x5, x6: (x2 and ((not x3 and (x4 if x5 else x6)) or (not x4 and not x5))) or (x3 and not x2 and (x4 or x5)),
        lambda x2, x3, x4, x5, x6: (x2 and ((x5 and not x3) or (not x4 and not x5 and not x6))) or (not x2 and ((x3 and ((x4 and x6) or not x5)) or (x4 and x6 and not x5))) or (x5 and not x3 and not (x4 and x6)),
        lambda x2, x3, x4, x5, x6: (not x5 and ((x2 and not x4) or (x3 and x6 and not x2))) or (x4 and ((not x2 and ((not x3 and (x5 or not x6)) or (x5 and not x6))) or (x5 and not x3 and not x6))) or (not x3 and not x4 and x5 and x6),
        lambda x2, x3, x4, x5, x6: (x2 and x3 and not x4 and not x5) or (x2 and not x3 and x4)
    ])

    return "".join("000000" if ch == " " else "000001" + cmap(ch.lower()) if ch.isupper() else cmap(ch) for ch in pl)

print(*[sol(c) for c in "aBCdefghijklmnopqrstuvwxyz"])
