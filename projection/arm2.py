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
        self._fr = 0.01


    def update(self, f):
        self.theta_ddot = (l*f - self._dm*g*math.sin(self.theta)-self._fr*self.theta_dot)/self._JZ
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

measures = 10000
t = np.linspace(0, measures-1, measures)
arm = Arm()
# for i in range(len(t)):
#     t = float(input("Enter force: "))
#     theta = arm.final_state(t, plot=True)
#     print(f"force: {t}, theta: {theta}")
#     h[i] = np.array([np.sin(theta[0])])



postemp = []
f=1
fs = []
for i in range(len(t)):
    if i>1/DT:
        f=0
    arm.update(f)
    fs.append(f)
    postemp.append(arm.get_state())
    print(arm.get_state())
pos = np.array(postemp)
theta = pos[:, 0]
thetadotdot = pos[:, 2]
H = np.stack([np.ones_like(theta)*f*l, -g*np.sin(theta)], axis=-1)

res =  np.linalg.inv(H.T @ H) @ H.T @ thetadotdot

# # 5, 10, 1, 3
# theta = [0.78, 0.67, -0.04, -0.55]

# thetadotdot = [-1.90, -0.1, 10, 1]

# 3.075 1.365
# theta = [-0.3345, 0.104, 0.5425, 1.324, -0.6672, -1.032, -0.2883, 0.2697]
# thetadotdot = [7.242, 0.5396,-9.048, -6.03, 10.88, 15.53, 5.344, -5.374]

print(res)

print(f"JZ = {1/res[0]}, dm = {res[1]/res[0]}")
pass
plt.plot(t, theta, "green")

# approx = h @ y

# plt.plot(t, approx, "red")

plt.show()
