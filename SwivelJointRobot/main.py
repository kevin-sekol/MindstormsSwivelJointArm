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

import time
import sys

import diagnosis

# Placeholder function definitons:
def returnToBase():
    global return_to_base
    return_to_base = True
    base_module_motor.run_angle(500, base_module_motor.angle() * -1)
    second_module_motor.run_angle(500, second_module_motor.angle() * -1)
    return_to_base = False

# Initialize the EV3 Brick.
ev3 = EV3Brick()
MODE = 1

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
return_to_base = False

# Return to base position
base_module_motor.run_target(500, base_position)
second_module_motor.run_target(500, second_position)
returnToBase()

# Reset motor angles
base_module_motor.reset_angle(0)
second_module_motor.reset_angle(0)

# Diagnosis (mode)
if MODE >= 1:
    diagnosis.diagnosis(MODE)

if len(sys.argv) > 1:
    diagnosis_mode = int(sys.argv[1])
    diagnosis.diagnosis(diagnosis_mode)

# Loop
while True:
    # Check for input
    pressed_buttons = receiver.keypad()
    if Button.BEACON in receiver.buttons(1): pressed_buttons.append(Button.BEACON)

    # Return to base position
    if Button.BEACON in pressed_buttons:   
        returnToBase()
    
    if return_to_base:
        continue

    # Base module: Move right (Left-Up pressed)
    if Button.LEFT_UP in pressed_buttons and Button.LEFT_DOWN not in pressed_buttons and not Button.BEACON in pressed_buttons:
        base_module_motor.run(500)  # Run motor at 500 degrees per second
    # Base module: Move left (Left-Down pressed)
    elif Button.LEFT_DOWN in pressed_buttons and Button.LEFT_UP not in pressed_buttons and not Button.BEACON in pressed_buttons:
        base_module_motor.run(-500)  # Run motor at -500 degrees per second
    elif return_to_base:
        continue
    else:
        base_module_motor.stop()  # Stop the motor when no button is pressed

    # Second module: Move right (Right-Up pressed)
    if Button.RIGHT_UP in pressed_buttons and Button.RIGHT_DOWN not in pressed_buttons and not Button.BEACON in pressed_buttons:
        second_module_motor.run(500)  # Run motor at 500 degrees per second
    # Second module: Move left (Right-Down pressed)
    elif Button.RIGHT_DOWN in pressed_buttons and Button.RIGHT_UP not in pressed_buttons and not Button.BEACON in pressed_buttons:
        second_module_motor.run(-500)  # Run motor at -500 degrees per second
    elif return_to_base:
        continue
    else:
        second_module_motor.stop()  # Stop the motor when no button is pressed

# Play another beep sound.
ev3.speaker.beep(frequency=1000, duration=500)