from hub import motion_sensor, port
import runloop
import motor_pair
import motor
motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

def move_forward(forward_velocity):
    turn = (0 + motion_sensor.tilt_angles()[0]/10)
    motor_pair.move(motor_pair.PAIR_1, int(turn), velocity=forward_velocity, acceleration=100)

    

def move_degrees (velocity,rotation):
    motor.reset_relative_position(port.B, 0)
    while motor.relative_position(port.B) /360 < rotation:
        move_forward(velocity)
    motor.stop(motor_pair.PAIR_1)
    
move_degrees(500,2)
