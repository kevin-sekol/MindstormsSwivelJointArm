from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

def diagnosis(mode):
    # Initialize remote control
    receiver = InfraredSensor(Port.S2)

    # Test import response time from remote keypad
    if mode == 1:
        print("Starting keypad response test (mode 1).")

    while mode == 1:
        start = time.time()
        pressed_buttons = receiver.keypad()
        elapsed = time.time() - start
        print(f"Keypad read time: {elapsed:.3f} seconds")
        wait(10)

    # Test infrared channel
    if mode == 2:
        print("Starting IR channel test (mode 2).")
        
    while mode == 2:
        print(f"IR Channel: {receiver.channel}")
