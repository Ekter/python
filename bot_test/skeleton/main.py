from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_D, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.led import Leds


tank_drive = MoveTank(OUTPUT_B, OUTPUT_D)

color_sensor = ColorSensor()
start = False
i= 0
while not start:
    ambient_light = color_sensor.ambient_light_intensity
    i=i*0.9+ambient_light*0.1
    red_color = color_sensor.red
    print(ambient_light, red_color,i)

    if i > 30:
        while not start:
            ambient_light = color_sensor.ambient_light_intensity
            red_color = color_sensor.red
            # print(ambient_light, red_color)
            if ambient_light <20:
                start = True
                break


gyro = GyroSensor()
ultrasonic_sensor = UltrasonicSensor()

K = -0.01

gyro.reset()
while ultrasonic_sensor.distance_centimeters>20:
    angle = gyro.angle
    rl_unnorm = 0.5-K*angle
    rr_unnorm = 0.5+K*angle
    if max(rr_unnorm, rl_unnorm) == rr_unnorm:
        rl_norm = rl_unnorm/rr_unnorm
        rr_norm = rr_unnorm/rr_unnorm
    else:
        rr_norm = rr_unnorm/rl_unnorm
        rl_norm = rl_unnorm/rl_unnorm

    tank_drive.on(SpeedPercent(rr_norm*100), SpeedPercent(rl_norm*100))

tank_drive.on(SpeedPercent(0), SpeedPercent(0))

