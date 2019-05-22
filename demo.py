# demo.py
# demonstrate various inputs of the circuit playground express

from adafruit_circuitplayground.express import cpx

# single tap detection
cpx.detect_taps = 1

# set touch thresholds
cpx.adjust_touch_threshold(200)

while True:
    
    # movement
    x, y, z = cpx.acceleration
    
    # light sensor
    light = cpx.light
    
    # temperature in Celcius
    temperature_c = cpx.temperature

    print("x:{} y:{} z:{} light:{} temperature_c:{}".format(x, y, z, light, temperature_c))
    
    # shake detection
    if cpx.shake(shake_threshold=15):
        print("shake detected")
        
        # turn off red led
        cpx.red_led = False
        
        # turn all pixels off
        for i in range(10):
            cpx.pixels[i] = [0, 0, 0]
            
        # stop tones
        cpx.stop_tone()

    # detect tap
    if cpx.tapped:
        print("tap detected")

    # press button A
    if cpx.button_a:
        
        # turn first pixel blue
        cpx.pixels[0] = [0, 0, 3]
        
        # turn on red LED
        cpx.red_led = True
    
    
    # press button B
    if cpx.button_b:
        
        # if switch is left or right
        if cpx.switch:
            
            # play laugh
            cpx.play_file("laugh.wav")
            
        else:
            
            # play rimshot
            cpx.play_file("rimshot.wav")

    # detect touches
    if cpx.touch_A1:
        print("Touched pad A1")
        cpx.pixels[1] = [1, 0, 0]
        
    if cpx.touch_A2:
        print("Touched pad A2")
        cpx.pixels[2] = [0, 1, 0]
        
    if cpx.touch_A3:
        print("Touched pad A3")
        cpx.pixels[3] = [0, 0, 1]
        
    if cpx.touch_A4:
        print("Touched pad A4")
        cpx.pixels[4] = [1, 1, 0]
        
    if cpx.touch_A5:
        print("Touched pad A5")
        cpx.pixels[5] = [1, 1, 1]
        cpx.start_tone(230)
        
    if cpx.touch_A6:
        print("Touched pad A6")
        cpx.pixels[6] = [2, 1, 1]
        cpx.start_tone(260)
        
    if cpx.touch_A7:
        print("Touched pad A7")
        cpx.pixels[7] = [3, 3, 3]
        cpx.start_tone(294)

