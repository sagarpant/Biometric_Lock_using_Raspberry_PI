import time
import RPi.GPIO as GPIO


class LockOutput:
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(13, GPIO.OUT)

    def main (self):
        timestamp1 = time.time()
        while (time.time() - timestamp1) <= 5:
            GPIO.output(13, 1)
            time.sleep(0.1)
        GPIO.output(13, 0)
