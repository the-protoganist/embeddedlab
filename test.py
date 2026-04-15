import RPi.GPIO as GPIO
import time

LED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

try:
    while True:
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(LED,GPIO.LOW)
        time.sleep(2)
except KeyboardInterrupt:
    print('Bye')
finally:
    GPIO.cleanup()