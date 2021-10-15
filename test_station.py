import logging
import time

import RPi.GPIO as GPIO


def test_vibration(vibrations):
    for i in range(10):
        logging.info("Vibrate!!!")
        GPIO.output(vibrations, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(vibrations, GPIO.LOW)
        time.sleep(0.2)

    GPIO.cleanup()


def test_sound(sound):
    for i in range(10):
        input = GPIO.input(sound)
        logging.info(input)


if __name__ == '__main__':
    vibrations = 37
    sound = 15
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(vibrations, GPIO.OUT)
    GPIO.setup(sound, GPIO.IN)

    test_sound(sound)
