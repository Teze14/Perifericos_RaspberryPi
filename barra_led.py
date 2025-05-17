from gpiozero import LEDBarGraph
from time import sleep

# Pines en orden invertido
graph = LEDBarGraph(12, 13, 14, 15, 16, 17, 18, 19, 20, 21)

try:
    while True:
        for i in range(10):  # encendido
            graph.value = i / 10
            sleep(0.5)
        for i in reversed(range(10)):  # apagado
            graph.value = i / 10
            sleep(0.5)
except KeyboardInterrupt:
    graph.off()
    print("apagado")"

encooder rotacional:
"from gpiozero import RotaryEncoder
from signal import pause

encoder = RotaryEncoder(a=5, b=6, max_steps=100)

def posicion():
    print(f"Posición actual: {encoder.steps}")

encoder.when_rotated = posicion

print("gira la perilla")
pause()
