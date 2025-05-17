from RPLCD.i2c import CharLCD
from time import sleep

#creamos el objeto lcd
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2,
                          charmap='A00', auto_linebreaks=True)

lcd.clear()
lcd.write_string("Para un tutorial")
sleep(1)
lcd.clear()
lcd.write_string("Like y Suscribete")"

servo: 

"from gpiozero import Servo
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
    pass"
