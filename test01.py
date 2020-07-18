import grovepi
import time


# digital write
grovepi.digitalWrite(2,1)
grovepi.digitalWrite(5,0)

# read temp
grovepi.temp(7)
grovepi.dht(7,0)

# module_type:
#             DHT11 0
#             DHT22 1
#             DHT21 2
#             DHT2301 3

# read ultrasonic
grovepi.ultrasonicRead(4)

import grove_rgb_lcd as grove_rgb_lcd
# set background to red, green and blue
lcd.setRGB(200,0,0)
lcd.setRGB(0,200,0)
lcd.setRGB(0,0,200)

# write text to RGB
lcd.setText('Hello There')
lcd.setRGB(255,113,181)

def ReadDHTandText(dhtport=7): 
    [t,h] = grovepi.dht(dhtport,0)
    msg = f'temp: {t}C\nhumidity: {h}%'
    print(msg)
    lcd.setText_norefresh(msg)


def FadeLed(pin=5):
    # set pin mode to output
    grovepi.pinMode(pin,'OUTPUT')
    pinOutRange = range(0,100,15)
    for o in pinOutRange: 
        print(o)
        grovepi.analogWrite(pin,o)
        time.sleep(1)

while True: ReadDHTandText(); time.sleep(1)

