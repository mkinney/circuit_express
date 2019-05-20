let lastLevel = 0
let level = 0
let pixels = light.createStrip(pins.A1, 30)
let color = Colors.White
if (SwitchDirection.Left) {
    color = Colors.Blue
} else {
    color = Colors.White
}
forever(function () {
    level = input.soundLevel()
    if (lastLevel != level) {
        light.clear()
        pixels.clear()
        for (let i = 0; i <= pixels.length() / 255 * level - 14; i++) {
            pixels.setPixelColor(i, color)
        }
        for (let j = 0; j <= 10 / 255 * level - 5; j++) {
            light.setPixelColor(j, color)
        }
        lastLevel = level
    }
})

