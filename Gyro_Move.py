from hub import port
import motor_pair
import motor
from hub import port
from hub import motion_sensor

motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
#This part is to turn the robot
def turn(angle):
    if angle <0:
        while motion_sensor.tilt_angles()[0] > angle:
            motor_pair.move(motor_pair.PAIR_1, 100, velocity=100)
        motor_pair.stop(motor_pair.PAIR_1)
    else:
        while motion_sensor.tilt_angles()[0] < angle:
            motor_pair.move(motor_pair.PAIR_1, -100, velocity=100)
        motor_pair.stop(motor_pair.PAIR_1)
#This is to set how much you want to turn
turn(900)

#this part is to make it move forward
def forward(angle, speed, rotation):
    motor.reset_relative_position(port.B, 0)
    while motor.relative_position(port.B)/360 < rotation :
        motor_pair.move(motor_pair.PAIR_1, int(angle + (motion_sensor.tilt_angles()[0])/10), velocity=speed, acceleration=1000)
    motor.stop(motor_pair.PAIR_1)
#This is to set how far you want to go
forward(0, 500, 3)
