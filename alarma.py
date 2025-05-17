from gpiozero import Buzzer, Button
from time import sleep
from signal import pause

sensor_sonido = Button(17)

print("esperando...")
pause()
zumbador = Buzzer(18)

def detectar():
    print("Sonido detectado")

sensor_sonido.when_pressed = detectar

try:
    while True:
        if sensor_sonido.is_pressed:
            zumbador.on()
            sleep(0.1)
            zumbador.off()
            sleep(0.1)
        else:
            zumbador.off()
            sleep(0.1)

except KeyboardInterrupt:
    zumbador.off()
