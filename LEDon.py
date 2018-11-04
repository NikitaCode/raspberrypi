import PRi.GPIO as GPOI
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarning(false)
GPIO.setup(18,GPIO.OUT)
print('LED On')
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print('LED Off')
GPIO.output(18,GPIO.LOW)
