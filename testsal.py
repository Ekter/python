import matplotlib.pyplot as plt
import numpy as np


def sal1(y):
    return (100_000+20_000*int(y/12))/12

def sal2(y):
    return (50_000+5_000*int(y*2/12))/6

t = 0

a1 = []
a2 = []


while t < 20*12:
    a1.append(sal1(t))
    a2.append(sal2(t))
    t += 1
    print(t)


plt.plot(np.arange(0, 20, 1/12), a1, label="year-based")
plt.plot(np.arange(0, 20, 1/12), a2, label="semester-based")
plt.xlabel("year")
plt.legend()
plt.show()

c1 = np.cumsum(a1)
c2 = np.cumsum(a2)

plt.plot(np.arange(0, 20, 1/12), c1, label="year-based")
plt.plot(np.arange(0, 20, 1/12), c2, label="semester-based")
plt.xlabel("year")
plt.legend()
plt.show()

