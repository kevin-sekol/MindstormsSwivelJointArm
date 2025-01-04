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
receiver = InfraredSensor(Port.S1)

# Write your program here

# Play a sound.
ev3.speaker.beep()

# First parameter: speed (Degrees per second), second parameter: target angle
# Base module
#for i in range(10):
    #base_module_motor.run_target(500, 3600)

#for i in range(10):
    #base_module_motor.run_target(500, -3600)

# Second module
#for i in range(10):
    #second_module_motor.run_target(500, 3600)

#for i in range(10):
    #second_module_motor.run_target(500, -3600)

# Loop
while True:
    # Check for input
    print(receiver.keypad()) 
    pressed_buttons = []
    for value in receiver.keypad():
        pressed_buttons.append(value)

    # Left-Up pressed
    if Button.LEFT_UP in pressed_buttons and not Button.LEFT_DOWN in pressed_buttons:
        # Base module motor right
        base_module_motor.run_target(500, 100)
        print("l-up")

    # Left-Down pressed
    if Button.LEFT_DOWN in pressed_buttons and not Button.LEFT_UP in pressed_buttons:
        # Base module motor left
        base_module_motor.run_target(500, -100)
        print("l-down")

    # Right-Up pressed
    if Button.RIGHT_UP in pressed_buttons and not Button.RIGHT_DOWN in pressed_buttons:
        # Second module motor right
        second_module_motor.run_target(500, 100)
        print("r-up")

    # Right-Down pressed
    if Button.RIGHT_DOWN in pressed_buttons and not Button.RIGHT_UP in pressed_buttons:
        # Second module motor left
        second_module_motor.run_target(500, -100)
        print("r-down")


#print(pressed_buttons)
#print(receiver.keypad())

# Play another beep sound.
ev3.speaker.beep(frequency=1000, duration=500)

