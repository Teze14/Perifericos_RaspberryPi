from gpiozero import Buzzer
from time import sleep

zumbador = Buzzer(18)

try:
    while True:
        zumbador.on()
        sleep(0.1)
        zumbador.off()
        sleep(0.1)
except KeyboardInterrupt:
    zumbador.off()
