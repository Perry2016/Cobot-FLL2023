from hub import motion_sensor, port
import motor_pair
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)
add = 30
def move_forward(vel):
    turn = (0 + motion_sensor.tilt_angles()[0])/2
    motor_pair.move(motor_pair.PAIR_1, int(turn), velocity=vel, acceleration=100)
    print(motion_sensor.tilt_angles()[0])

def turn(amount):
    if amount < 0:
        while motion_sensor.tilt_angles()[0] > amount:
            motor_pair.move(motor_pair.PAIR_1, 100, velocity=100)
        motor_pair.stop(motor_pair.PAIR_1)
    else:
        while motion_sensor.tilt_angles()[0] < amount:
            motor_pair.move(motor_pair.PAIR_1, -100, velocity=100)
        motor_pair.stop(motor_pair.PAIR_1)

while True:
    turn(900-add)
