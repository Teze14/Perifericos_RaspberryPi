from gpiozero import Servo
from time import sleep

# Crear instancia del servo (GPIO17 = pin físico 11)
servo = Servo(17)

try:
    while True:
        servo.min()   # 0 grados aprox
        sleep(1)
        servo.mid()   # 90 grados aprox
        sleep(1)
        servo.max()   # 180 grados aprox
        sleep(1)

except KeyboardInterrupt:
    pass
