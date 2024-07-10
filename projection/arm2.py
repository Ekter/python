DT = 0.001
g = 9.81
l = 0.65
import math
import time


class Arm:
    def __init__(self) -> None:
        self.theta = 0
        self.theta_dot = 0
        self.theta_ddot = 0
        self._JZ = 0.0576
        self._dm = 0.22*0.48


    def update(self, f):
        self.theta_ddot = (l*f - self._dm*g*math.sin(self.theta))/self._JZ
        self.theta_dot += self.theta_ddot * DT
        self.theta += self.theta_dot * DT

    def get_state(self):
        return self.theta, self.theta_dot, self.theta_ddot

    def final_state(self,f, plot=False):
        if plot:t = np.linspace(0, 100000, 100001)
        if plot:postemp = np.zeros((100001, 3))
        for i in range(100000):
            self.update(f)
            if plot:postemp[i, ...] = self.get_state()

        if plot:plt.plot(t, postemp)
        if plot:plt.show()
        return self.get_state()




import numpy as np
import matplotlib.pyplot as plt

measures = 1000
t = np.linspace(0, measures-1, measures)
h = np.zeros(6,)
arm = Arm()
for i in range(len(t)):
    t = float(input("Enter force: "))
    theta = arm.final_state(t, plot=True)
    print(f"force: {t}, theta: {theta}")
    h[i] = np.array([np.sin(theta[0])])



# postemp = []

# for i in range(len(f)):
#     arm.update(1)
#     postemp.append(arm.get_state()[0])

#     print(arm.get_state())
# pos = np.array(postemp)
# N = 1
# h = np.stack([f**n for n in range(N, -1, -1)], axis=-1)

y = np.linalg.inv(h.T @ h) @ h.T @ t

print(y)

plt.plot(t, y, "green")

approx = h @ y



plt.plot(t, approx, "red")

plt.show()
