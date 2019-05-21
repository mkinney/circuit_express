let level = 0
let pixels = light.createStrip(pins.A1, 30)
let color = Colors.White
let sens = 120
pixels.setBrightness(255)
light.setBrightness(255)
forever(function () {

    if (input.buttonA.isPressed()) {
        sens = sens - 5
    }
    if (input.buttonB.isPressed()) {
        sens = sens + 5
    }

    if (input.switchRight()) {
        sens = 0
    }

    level = input.soundLevel()
    color = Colors.Black
    if (level > sens) {
        color = Colors.Blue
    }
    for (let k = 0; k <= pixels.length(); k++) {
        pixels.setPixelColor(k, color)
    }
    for (let l = 0; l <= 10; l++) {
        light.setPixelColor(l, color)
    }
})

