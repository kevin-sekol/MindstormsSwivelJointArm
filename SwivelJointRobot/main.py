#!/usr/bin/env pybricks-micropython
# Shebang line on top to choose correct interpreter 

# Import pybricks functions
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motors
base_module_motor = Motor(Port.A)
second_module_motor = Motor(Port.B)

# Initialize remote control
receiver = InfraredSensor(Port.S2)

# Write your program here

# Play a sound.
ev3.speaker.beep()

# Initialize target positions
base_position = 0
second_position = 0

# Loop
while True:
    # Check for input
    pressed_buttons = receiver.keypad()

    # Base module: Move right (Left-Up pressed)
    if Button.LEFT_UP in pressed_buttons and Button.LEFT_DOWN not in pressed_buttons:
        base_module_motor.run(500)  # Run motor at 500 degrees per second
    # Base module: Move left (Left-Down pressed)
    elif Button.LEFT_DOWN in pressed_buttons and Button.LEFT_UP not in pressed_buttons:
        base_module_motor.run(-500)  # Run motor at -500 degrees per second
    else:
        base_module_motor.stop()  # Stop the motor when no button is pressed

    # Second module: Move right (Right-Up pressed)
    if Button.RIGHT_UP in pressed_buttons and Button.RIGHT_DOWN not in pressed_buttons:
        second_module_motor.run(500)  # Run motor at 500 degrees per second
    # Second module: Move left (Right-Down pressed)
    elif Button.RIGHT_DOWN in pressed_buttons and Button.RIGHT_UP not in pressed_buttons:
        second_module_motor.run(-500)  # Run motor at -500 degrees per second
    else:
        second_module_motor.stop()  # Stop the motor when no button is pressed

# Play another beep sound.
ev3.speaker.beep(frequency=1000, duration=500)

