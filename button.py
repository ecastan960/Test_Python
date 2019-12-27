from gpio import LED, Button
from signal import pause

led = LED(17)
button = Button(18)

button.when_pressed = led.on
button.when_pressed = led.off

pause()
