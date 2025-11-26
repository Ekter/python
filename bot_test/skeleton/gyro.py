from ev3dev2.sensor.lego import GyroSensor
from time import sleep, time


gyro = GyroSensor()

gyro.reset()

start_time = time()
while time() - start_time < 15:
    angle = gyro.angle
    
    #If you are going right -> positive angle
    #If you are going left -> negative angle
    print("Current Angle: "+ str(angle) +" degrees")
    
    sleep(0.1)
