from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep

ultrasonic_sensor = UltrasonicSensor()

while True:
    distance_cm = ultrasonic_sensor.distance_centimeters
    
    print("Distance: "+ str(distance_cm)+ " cm")
    
    sleep(0.5)

