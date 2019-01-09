import RPi.GPIO as GPIO
import time

pinArray = [5, 6, 13, 19, 26]
currentLED = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for x in pinArray:
    GPIO.setup(x,GPIO.OUT)
    GPIO.output(18,0)

GPIO.output(pinArray[currentLED],1)

counter = 1
i = 1
# while i < 9999:
#     i += 1
#     if counter==1:
#         nameOne=input("LED on? Y/N")
#         if nameOne=='y':
#             GPIO.output(18,GPIO.HIGH)
#             counter+=1
#         if not nameOne=='y':
#             GPIO.output(18,GPIO.LOW)
#
#
#     if counter==2:
#         nameTwo = input('Turn LED Off? Y/N')
#         if nameTwo=='y':
#             GPIO.output(18,GPIO.LOW)
#             counter-=1
#         if not nameTwo=='y':
#             GPIO.output(18,GPIO.HIGH)
