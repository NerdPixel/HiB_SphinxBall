import logging
import time

import RPi.GPIO as GPIO

if __name__ == '__main__':
    vibrations = 26

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(vibrations, GPIO.OUT)

    for i in range(10):
        logging.info("Vibrate!!!")
        GPIO.output(vibrations, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(vibrations, GPIO.LOW)
        time.sleep(0.2)

    GPIO.cleanup()