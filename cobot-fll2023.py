from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Move straight at default velocity for 360 degrees
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 360, 1000, 1000)

    # Turn right for 180 degrees
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 180, 0, 1000)

    # Perform tank turn for 720 degrees
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1, 720, 1000, -1000)

runloop.run(main())
