import ftprci as fci

# import time
import matplotlib.pyplot as plt
import math


class System:
    def __init__(self):
        self.R = 5.5
        self.C = 3
        self.Tmes = 18.0
        self.Text = 12.0
        self.Pconst = -30.0

    def command(self, pchauf: float):
        self.Tmes = (
            (1 - 1 / (self.R * self.C)) * self.Tmes
            + 1 / (self.R * self.C) * self.Text
            + 1 / (self.C) * (self.Pconst + pchauf)
        )

    def read(self, t: float = 0):
        return self.Tmes


th_system = System()

pid = fci.PIDController(3, 3, 0, fci.DiscreteIntegral.EulerF(dt=1))

fig0 = plt.figure(0)
fig1 = plt.figure(1)
fig2 = plt.figure(2)

ax0 = fig0.add_subplot()
ax0.set_title("Temperature actuelle")
ax0.set_xlabel("Time (s)")
ax0.set_ylabel("Temperature (°C)")

ax1 = fig1.add_subplot()
ax1.set_title("Consigne")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Control Signal")

ax2 = fig2.add_subplot()
ax2.set_title("Temperature souhaitee")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Temperature (°C)")

c = fci.Clock(1 / 100, 2)
p = fci.ProgressBar(c)

log = fci.logger.ClockedPlotLogger1D(c, [ax0], update_freq=math.nan)
log2 = fci.logger.ClockedPlotLogger1D(c, [ax1], update_freq=math.nan)
log3 = fci.logger.ClockedPlotLogger1D(c, [ax2], update_freq=math.nan)


pid.set_order(21)

new_order = lambda t: (pid.set_order(18 + 5 * math.cos(2 * math.pi * t / 2)), t, pid.order)[2]

c >> p | new_order | log3 | th_system.read | log | pid | log2 | th_system.command
c.start()


c.wait()
log.plot()
log2.plot()
log3.plot()
# log.
plt.show()

# while c.timer.running:

#     current_temp = th_system.read()
#     control_signal = pid(current_temp)
#     th_system.command(control_signal)
#     # print(f"Current Temperature: {current_temp:.2f} °C, Control Signal: {control_signal:.2f}")
#     log.log(current_temp)
#     log2.log(control_signal)

#     time.sleep(1)
#     c.step()
