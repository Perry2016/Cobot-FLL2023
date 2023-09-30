from hub import port
import runloop
import motor_pair
import motor
async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    await motor.run_for_degrees(port.A, -120, 500, acceleration=100, deceleration=100)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 1150, 500, 500)
    motor.run_for_degrees(port.D, -270, 800, acceleration=100, deceleration=100)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, -50, 50, 50)
    await motor.run_for_degrees(port.B, -120, 500, acceleration=100, deceleration=100)

runloop.run(main())
