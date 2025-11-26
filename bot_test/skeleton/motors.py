from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_D, SpeedPercent
import time


tank_drive = MoveTank(OUTPUT_B, OUTPUT_D)

# Define a function to keep the robot moving straight using the gyro
def move_straight_for_seconds(seconds, speed=100):
    start_time = time.time()
    while time.time() - start_time < seconds:
        tank_drive.on(SpeedPercent(speed), SpeedPercent(speed))
    
    # Stop the motors after the loop
    tank_drive.off()

# Move straight for 1 second at maximum speed
move_straight_for_seconds(1, speed=100)
