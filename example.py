#/usr/bin/python3
prix = 150
int(input("prix ? "))
if prix > 1000 :
   print("trop cher")
   print("j'achète pas")
else :
    print("j'achète")
    if prix < 100 :
       print("c'est donné!")
    else :
        print("même si c'est pas donné")
print("fin des achats")  