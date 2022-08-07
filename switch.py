# Import required modules
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

GPIO.setup(2, GPIO.OUT)

GPIO.output(2, GPIO.HIGH)

time.sleep(10)

GPIO.output(2, GPIO.LOW)


