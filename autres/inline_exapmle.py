# a=4
# b=6
# print(a+b)
# print(a*b)


n = 10
for i in range(n):
    print(i)
    if i == 5:
        print("caca")


(lambda: ((print(i), print("caca") if i == 5 else None) for i in range(n)))()
((print(i), print("caca") if i == 5 else None) for i in range(n))