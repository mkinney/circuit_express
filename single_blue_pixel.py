# single_blue_pixel.py
from adafruit_circuitplayground.express import cpx

print("Hello")
while True:
    cpx.pixels[0] = [0, 0, 3]
