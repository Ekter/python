import time

n = 10**int(input("power of 10: "))

t_start = time.time()

n1 = 0
n2 = 1

c = 0

while c<n:
    n2, n1 = (n1+n2)%1000000007, n2
    c += 1

t_end = time.time()
print(f"Fibonacci number F({n}) is {n2}")
print(f"Computation time: {t_end - t_start} seconds")
