import RPi.GPIO as GPIO
import time

pinArray = [5, 6, 13, 19, 26]
currentLED = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for x in pinArray:
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(x,0)

# GPIO.output(pinArray[currentLED],1)

while True:
    i += 1
    nameOne=input("Move Left or Rigth (L / R)")
    if nameOne=='l':
        currentLED -= 1
        GPIO.output(pinArray[currentLED],GPIO.HIGH)
    else if nameOne =='l':
        GPIO.output(pinArray[currentLED],GPIO.HIGH)
        currentLED += 1



    # nameTwo = input('Turn LED Off? Y/N')
    # if nameTwo=='y':
    #     GPIO.output(18,GPIO.LOW)
    #     counter-=1
    # if not nameTwo=='y':
    #     GPIO.output(18,GPIO.HIGH)
