import time
import adafruit_dht
import board

#Crear objeto de sensor DHT11 usando GPIO 4
dht_device = adafruit_dht.DHT11(board.D4)

try:
    while True:
        temperatura = dht_device.temperature
        humedad = dht_device.humidity
        print(f"Temperatura: {temperatura}°C Humedad: {humedad}%")
        time.sleep(2)
except KeyboardInterrupt:
    print("Lectura detenida por el usuario.")
except RuntimeError as error:
    print(f"Error de lectura: {error}")
