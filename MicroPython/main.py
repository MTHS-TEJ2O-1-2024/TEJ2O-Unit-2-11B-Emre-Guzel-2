"""
Created by: Emre Guzel
Created on: Oct 23 2024
This module is a Micro:bit MicroPython program generates random number from 0-99 and tells us the picked number is bigger and small  
"""

from microbit import *
import random

# Setting the program
display.clear
display.show(Image.HAPPY)

# Setting the veribles
num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

# Setting the button A and making the that to genreate a number between 0 and 99
while True:
    if button_a.is_pressed():
        display.clear
        display.scroll("#1")
        display.scroll(num1)
        sleep(500)
        display.show(Image.HAPPY)

    # Setting the button B and making the that to genreate a number between 0 and 99
    if button_b.is_pressed():
        display.clear
        display.scroll("#2")
        display.scroll(num2)
        sleep(500)
        display.show(Image.HAPPY)

    # Ading a shake functoin
    if accelerometer.was_gesture("shake"):
        display.clear
        if num1 < num2:
            display.scroll(num1)
            display.scroll("<")
            display.scroll(num2)

        if num1 > num2:
            display.scroll(num1)
            display.scroll(">")
            display.scroll(num2)
        display.show(Image.SAD)
