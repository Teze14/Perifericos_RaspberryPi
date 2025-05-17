from gpiozero import Button
from signal import pause

sensor_sonido = Button(17)

def detectar():
    print("Sonido detectado")

sensor_sonido.when_pressed = detectar

print("esperando...")
pause()
