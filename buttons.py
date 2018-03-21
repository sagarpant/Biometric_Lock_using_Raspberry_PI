import RPi.GPIO as GPIO


class Buttons:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def button_1(self):
        return not GPIO.input(19)

    def button_2(self):
        return not GPIO.input(26)
