from hub import motion_sensor, port
import motor_pair, motor
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
add = 30

def turn(amount):
    if amount < 0:
        while motion_sensor.tilt_angles()[0] > amount:
            motor_pair.move(motor_pair.PAIR_1, 100, velocity=100)
        motor_pair.stop(motor_pair.PAIR_1)
    else:
        while motion_sensor.tilt_angles()[0] < amount:
            motor_pair.move(motor_pair.PAIR_1, -100, velocity=100)
        motor_pair.stop(motor_pair.PAIR_1)

def move_forward(angle, vel, rotations):
    motor.reset_relative_position
    while motor.relative_position(port.B) / 360 < rotations:
        turn = (angle + motion_sensor.tilt_angles()[0]/10)/2
        motor_pair.move(motor_pair.PAIR_1, int(turn), velocity=vel, acceleration=100)
    motor_pair.stop(motor_pair.PAIR_1)


move_forward(0, 300, 2)
