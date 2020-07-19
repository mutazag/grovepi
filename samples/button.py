import grovepi
import grove_rgb_lcd as lcd

button = 4
red = 5
blue = 6
relay = 2

grovepi.pinMode(button, 'INPUT')
grovepi.pinMode(red, 'OUTPUT')
grovepi.pinMode(blue, 'OUTPUT')
grovepi.pinMode(relay, 'OUTPUT')


while True:
    button_press = grovepi.digitalRead(button)


    if button_press == True: 
        grovepi.digitalWrite(red, 1)
        grovepi.digitalWrite(blue, 0)
        lcd.setRGB(200,0,0)
        lcd.setText_norefresh('Hi')
        grovepi.digitalWrite(relay,1)
    else: 
        grovepi.digitalWrite(red, 0)
        grovepi.digitalWrite(blue, 1)
        lcd.setRGB(0,0,200)
        lcd.setText_norefresh('GOObye')
        grovepi.digitalWrite(relay,0)


grovepi.ultrasonicRead()

