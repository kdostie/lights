# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel


# On CircuitPlayground Express, and boards with built in status NeoPixel -> board.NEOPIXEL
# Otherwise choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D1
pixel_pin0 = board.A0
pixel_pin1 = board.A1
pixel_pin2 = board.A2
pixel_pin3 = board.A3
# On a Raspberry pi, use this instead, not all pins are supported
# pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 47

RED = 30
GREEN = 30
BLUE = 250

MAX_BRIGHTNESS = 1.0

first_run = True

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

strip_0 = neopixel.NeoPixel(
    pixel_pin0, 
    num_pixels, 
    brightness = MAX_BRIGHTNESS, 
    auto_write=False,
    pixel_order=ORDER
)
strip_1 = neopixel.NeoPixel(
    pixel_pin1, 
    num_pixels, 
    brightness = MAX_BRIGHTNESS, 
    auto_write=False,
    pixel_order=ORDER
)
strip_2 = neopixel.NeoPixel(
    pixel_pin2, 
    num_pixels, 
    brightness = MAX_BRIGHTNESS, 
    auto_write=False,
    pixel_order=ORDER
)
strip_3 = neopixel.NeoPixel(
    pixel_pin3, 
    num_pixels, 
    brightness = MAX_BRIGHTNESS, 
    auto_write=False,
    pixel_order=ORDER
)

def setColorWBrightness(r, g, b, bright):
    r = int(r*bright)
    g = int(g*bright)
    b = int(b*bright)
    return (r, g, b)

def setPixelColor(pos, color):
    strip_0[pos] = color
    strip_1[pos] = color
    strip_2[pos] = color
    strip_3[pos] = color

def showAll():
    strip_0.show()
    strip_1.show()
    strip_2.show()
    strip_3.show()

while True:
    # First Time through the Loop do this
    if first_run == True:
        # Wait 5s then start lighting pixels. Added to eliminate the 10 start up lit before creeping 
        time.sleep(5)
        # Set the first run flag so this doesnt happen again
        first_run = False
        SABER_COLOR = setColorWBrightness(RED,GREEN,BLUE,MAX_BRIGHTNESS)
        
        for i in range(num_pixels):
            # Set Pixel Color
            setPixelColor(i, SABER_COLOR)
            # Update the Pixel
            showAll()
            # Wait 1.75s to do the next pixel
            time.sleep(1.75)
    #End of First Run
# This part will run every 30s to pulse the lightsaber
    # Wait 30s
    time.sleep(30)
    # Update the Color to be at 25% brightness 
    SABER_COLOR = setColorWBrightness(RED,GREEN,BLUE,0.25)
    # Loop Updates all pixels really quickly
    for i in range(num_pixels):
            setPixelColor(i, SABER_COLOR)
            showAll()
    # Wait .5s
    time.sleep(.5)
    # Update the Color to be at 25% brightness 
    SABER_COLOR = setColorWBrightness(RED,GREEN,BLUE,MAX_BRIGHTNESS)
    # Loop Updates all pixels really quickly
    for i in range(num_pixels):
            setPixelColor(i, SABER_COLOR)
            showAll()

