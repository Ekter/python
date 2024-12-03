from ev3dev2.sensor.lego import ColorSensor
from time import sleep

color_sensor = ColorSensor()

while True:
    ambient_light = color_sensor.ambient_light_intensity

    #Reading the starting light intensity will return a value close to 50 when the lights are red, 
    #Reading the starting light intensity will return a value close to 0 when the lights are off
    print("Ambient Light Intensity: ", ambient_light)

    sleep(0.5)
