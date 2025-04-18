# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin0 = board.A0

# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 47

SABER_COLOR = (30,30,250)

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

strip_0 = neopixel.NeoPixel(
    pixel_pin0, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def setPixelColor(pos, color):
    strip_0[pos] = color

def showAll():
    strip_0.show()

while True:
    for i in range(num_pixels):
        setPixelColor(i, SABER_COLOR)
        showAll()