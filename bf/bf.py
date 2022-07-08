#[ to make it more beautiful

pile=[0 for i in range(30000)]
cursor=0
with open("tests.b") as file:
    prg=file.read()
    print(prg)
    reader=0
    while reader<len(prg):
        i=prg[reader]
        if i=="+":
            pile[cursor]+=1
        elif i=="-":
            pile[cursor]-=1
        elif i==">":
            cursor+=1
        elif i=="<":
            cursor-=1
        elif i==".":
            print(chr(pile[cursor]),end="")
        elif i==",":
            temp=input()
            pile[cursor]=ord(temp) if len(temp)==1 else int(temp[1:])
        elif i=="[":
            if pile[cursor]==0:
                count=1
                while count > 0:
                    reader+=1
                    i=prg[reader]
                    if i=="[":
                        count+=1
                    elif i=="]":
                        count-=1
        elif i=="]":
            if pile[cursor]!=0:
                count=1
                while count > 0:
                    reader-=1
                    i=prg[reader]
                    if i=="]":
                        count+=1
                    elif i=="[":
                        count-=1
        reader+=1
        # print(reader)
        # print(pile)

