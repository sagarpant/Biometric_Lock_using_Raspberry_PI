import RPi.GPIO as GPIO
import time
 
class Irsens:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(5, GPIO.IN)
        #True when far
        #False when near

    def ir(self):
        return GPIO.input(5)
