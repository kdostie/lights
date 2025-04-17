# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import random

# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin0 = board.A0

# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 47

run_once = 0

SABER_COLOR = (30,30,250)

# Brightness
MIN_BRIGHTNESS = 0.1
MAX_BRIGHTNESS = 1.0
INCREASE_BY = .05

#Seconds to Wait Between Throbs
MIN_TIME_TO_WAIT=10
MAX_TIME_TO_WAIT=30

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

strip_0 = neopixel.NeoPixel(
    pixel_pin0, num_pixels, brightness=MAX_BRIGHTNESS, auto_write=False, pixel_order=ORDER
)


def setPixelColor(pos, color):
    strip_0[pos] = color

def showAll():
    strip_0.show()

def setPixelBrightness(pos, bright):
    strip_0[pos].brightness=bright


def setAllBrightness(bright, color):

    # Reset Colors
    for i in range(num_pixels):
        setPixelColor(i, color)
    strip_0.brightness = bright
    showAll()

while True:
    if run_once == 0:
        run_once = 1
        for i in range(num_pixels):
            setPixelColor(i, SABER_COLOR)
            showAll()
            # 0.001 is 1ms
            time.sleep(0.001)
    # Pick a random time to sleep be
    time.sleep(random.randint(MIN_TIME_TO_WAIT, MAX_TIME_TO_WAIT))
    # Pick a brightness to drop to
    brightness = random.uniform(MIN_BRIGHTNESS, MAX_BRIGHTNESS)
    setAllBrightness(brightness, SABER_COLOR)
