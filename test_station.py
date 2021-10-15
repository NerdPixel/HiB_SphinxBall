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
        print("test")
        input = GPIO.input(sound)
        logging.info(input)
        time.sleep(0.1)


if __name__ == '__main__':
    logging.basicConfig(filename='test_station.log', level=logging.INFO)
    vibrations = 37
    sound = 15
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(vibrations, GPIO.OUT)
    GPIO.setup(sound, GPIO.IN)
    test_vibration(vibrations)
    test_sound(sound)
