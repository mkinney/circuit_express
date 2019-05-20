# movement_based_lights.py
#   switch is white or blue lights
#   button a/b is to decrease/increase led brightness

import time
import board
import neopixel
from adafruit_circuitplayground.express import cpx

def was_movement(x, y, z, last_x, last_y, last_z):
    delta = 0.6
    retval = False
    try:
        tmpx = abs((x - last_x) / last_x)
        tmpy = abs((y - last_y) / last_y)
        tmpz = abs((z - last_z) / last_z)
    except:
        return retval
    #print("x:{} y:{} z:{} last_x:{} last_y:{} last_z:{}".format(x, y, z, last_x, last_y, last_z))
    #print("tmpx:{} tmpy:{} tmpz:{}".format(tmpx, tmpy, tmpz))
    if tmpx > delta or tmpy > delta or tmpz > delta:
        retval = True
    return retval

LED_COLOR = (0, 0, 255)
LED_NO_COLOR = (0, 0, 0)
brightness = 0.004
brightness_adjustment = 0.005

pixels = neopixel.NeoPixel(board.A1, 30, brightness=brightness, auto_write=False)

# set the last values before first time thru the loop
last_x, last_y, last_z = cpx.acceleration
movement = False
last_color = LED_NO_COLOR
color = LED_NO_COLOR

# turn off all NeoPixels on board
cpx.pixels.fill(color)
cpx.pixels.show()

# turn off all NeoPixes on external
pixels.fill(color)
pixels.show()

print("hello")

while True:
    x, y, z = cpx.acceleration
    movement = was_movement(x, y, z, last_x, last_y, last_z)

    if movement:
        # use the plotter in Mu
        #print(((1.0),))
        color = LED_COLOR
    else:
        #print(((0.0),))
        color = LED_NO_COLOR

    # only if color changed
    if last_color != color:
        cpx.pixels.fill(color)
        cpx.pixels.show()
        pixels.fill(color)
        pixels.show()

    if cpx.switch:
        # white
        LED_COLOR = (255, 255, 255)
    else:
        # blue
        LED_COLOR = (0, 0, 255)

    if cpx.button_a:
        brightness -= brightness_adjustment
        if brightness < 0:
            brightness = 0.0
    if cpx.button_b:
        brightness += brightness_adjustment
        if brightness > 1:
            brightness = 1.0

    cpx.pixels.brightness = brightness
    pixels.brightness = brightness

    time.sleep(0.01)
    last_x, last_y, last_z = x, y, z
    last_color = color