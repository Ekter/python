import os
lines = open("PeiP1/Projet_classes/Rogue3742/images.py").readlines()
output = open("PeiP1/Projet_classes/Rogue3742/images2.py","w")
lines_dics=[]
for index,l in enumerate(lines):
    if "= {" in l:
        lines_dics.append((index,l.strip().replace(" = {","")))

os.system("cd PeiP1/Projet_classes/Rogue3742/images/")
# cd PeiP1/Projet_classes/Rogue3742/images/
for dic,name_dic in lines_dics:
    line=""
    i=1
    # mkdir name_dic
    os.system(f"mkdir PeiP1/Projet_classes/Rogue3742/images/{name_dic}")
    while "}" not in line:
        line = lines[dic+i].strip()
        ll=line.replace("\"","").replace(",","")
        if ": " in ll:
            name,id=ll.split(": ")
            print(name,id)
            for l in lines:
                if id in l and "[" not in l and "]" not in l:
                    l2=l.split("\"")
                    os.system(f"mv PeiP1/Projet_classes/Rogue3742/images/{l2[1]} PeiP1/Projet_classes/Rogue3742/images/{name_dic}/{l2[1][:-4]}_{name}.png")
                    # mv l2[1] "name_dic/l2[1]_name"
                    l2[1]=name+"/"+l2[1]+"_"+name+"\n"
                    l2="\"".join(l2)
                    output.write(l2+"\n")
                    break
        i+=1
        line = lines[dic+i].strip()
