### circuit_express programs/learnings

See https://learn.adafruit.com/introducing-circuit-playground Neat little device.
Lots of sensors. Inexpensive. Can use python or javascript.

When you first get the device, it may have a demo program on it. 

## Python
1. Download Mu Editor - see https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor
2. Plug into USB
3. Get all 10 lights to show green. Copy the bin/adafruit-circuitpython-circuitplayground_express-en_US-4.0.0.uf2 or latest from https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython 
4. The device will reboot and then remount as CIRCUITPY drive.
5. Write your code in Mu editor and save to code.py.
6. Every time you save, it will reboot/reload code from code.py.
Note: See https://circuitpython.readthedocs.io/en/4.x/docs/index.html or https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/index.html or https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/CircuitPython_Essentials

## Drag and Drop (or Javascript)
1. Visit https://makecode.adafruit.com/#editor 
2. Create program
3. Click Save, which will download a .uf2 file
4. Plug in device
5. Get into boot mode (all green pixels)
6. Copy .uf2 file to device
7. Device will reboot and run code
Note: I seem to have to reboot mac every time I want to get the device in the "green" mode. Ugh.

## Sample programs

# loud_leds.js
(for high school marching band in parade) - It is "loud sound"-based. The LEDs all light up blue when a loud enough sound is heard. There are 2 buttons on that disc, so one increases the sensitivity of the loudness. The other button decreases the sensitivity. If that ends up not working out, we can slide the (really small) switch to have the lights always on bright blue. (without any sound detection) 

Videos of them in action:
<video width="420" height="315" controls><source src="loud_leds_in_action/IMG_5571.m4v" type="video/mp4">Your browser does not support video tag.</video>
<video width="420" height="315" controls><source src="loud_leds_in_action/IMG_5572.m4v" type="video/mp4">Your browser does not support video tag.</video>
<video width="420" height="315" controls><source src="loud_leds_in_action/IMG_5573.m4v" type="video/mp4">Your browser does not support video tag.</video>
<video width="420" height="315" controls><source src="loud_leds_in_action/IMG_5574.m4v" type="video/mp4">Your browser does not support video tag.</video>

# movement_based_lights.py
tried to limit movement to just up/down and have lights light up when there was movement. (prototype for parade)

# microphone_pixels_buttons.py
tried to use the microphone to detect "loudness" but was not successful (prototype for parade); used buttons for sensitivity

# microphone_and_pixels.py
tried to use the microphone to detect "loudness" but was not successful (prototype for parade)

# infared_buttons.py
detect each button on mini remote control (see https://www.adafruit.com/product/389 ); Note: You need to copy the lib/adafruit_irremote.mpy file (or download latest from https://github.com/adafruit/Adafruit_CircuitPython_IRRemote/releases)

# big_pixel.py
experiment with external pixel strip

# pixels_rainbow.py
experiment with pixels

# single_blue_pixel.py
show how to light a single pixel blue

# demo.py
demonstrate various inputs

# laugh.wav
sample file to play wave from demo.py

# rimshot.wav
sample file to play wave from demo.py
