from gpiozero import LED
from time import sleep

led= LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)"
Ultrasónico:
"from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=24, trigger=23, max_distance=1.0)

try:
    while True:
        distancia = sensor.distance * 100
        print(f"Distancia: {distancia:.3f} cm")
        sleep(1)

except KeyboardInterrupt:
    print("\n El usuario interrumpio la medicion.")
