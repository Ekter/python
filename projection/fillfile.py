with open("filefull.txt","w") as f:
    for i in range(999999):
        f.write(f"{i}"*100+"\n")
    f.close()