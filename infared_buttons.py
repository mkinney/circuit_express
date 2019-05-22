import pulseio
import board
import adafruit_irremote

# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

while True:
    pulses = decoder.read_pulses(pulsein)
    try:
        # Attempt to convert received pulses into numbers
        received_code = decoder.decode_bits(pulses, debug=False)
    except adafruit_irremote.IRNECRepeatException:
        # We got an unusual short code, probably a 'repeat' signal
        # print("NEC repeat!")
        continue
    except adafruit_irremote.IRDecodeException as e:
        # Something got distorted or maybe its not an NEC-type remote?
        # print("Failed to decode: ", e.args)
        continue

    print("NEC Infrared code received: ", received_code)
    if received_code == [255, 2, 255, 0]:
        print("Received NEC Vol-")
    if received_code == [255, 2, 127, 128]:
        print("Received NEC Play/Pause")
    if received_code == [255, 2, 191, 64]:
        print("Received NEC Vol+")
    if received_code == [255, 2, 223, 32]:
        print("Received NEC SETUP")
    if received_code == [255, 2, 95, 160]:
        print("Received UP")
    if received_code == [255, 2, 159, 96]:
        print("Received STOP/MODE")
    if received_code == [255, 2, 239, 16]:
        print("Received LEFT")
    if received_code == [255, 2, 111, 144]:
        print("Received ENTER SAVE")
    if received_code == [255, 2, 175, 80]:
        print("Received RIGHT")
    if received_code == [255, 2, 207, 48]:
        print("Received 0 10+")
    if received_code == [255, 2, 79, 176]:
        print("Received DOWN")
    if received_code == [255, 2, 143, 112]:
        print("Received REDO ARROW")
    if received_code == [255, 2, 247, 8]:
        print("Received 1")
    if received_code == [255, 2, 119, 136]:
        print("Received 2")
    if received_code == [255, 2, 183, 72]:
        print("Received 3")
    if received_code == [255, 2, 215, 40]:
        print("Received 4")
    if received_code == [255, 2, 87, 168]:
        print("Received 5")
    if received_code == [255, 2, 151, 104]:
        print("Received 6")
    if received_code == [255, 2, 231, 24]:
        print("Received 7")
    if received_code == [255, 2, 103, 152]:
        print("Received 8")
    if received_code == [255, 2, 167, 88]:
        print("Received 9")