#!/usr/bin/env python3
import time
import logging
import json
from random import randrange
import LCD as LCD
import board
import adafruit_mpu6050
from adafruit_extended_bus import ExtendedI2C as I2C


def choose_random_question():
    data = json.load(open('example-questions.json'))
    return data[randrange(len(data))]["frage"]


def gyro_changed():
    i2c = I2C(4)  # Device is /dev/i2c-4
    mpu = adafruit_mpu6050.MPU6050(i2c)
    while True:
        print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
        print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
        print("Temperature: %.2f C" % mpu.temperature)
        print("")
        time.sleep(1)


def display_question(question):
    LCD.setRGB(0, 255, 0)
    LCD.setText(question)


def start_loop():
    while True:
        if gyro_changed():
            question = choose_random_question()
            logging.info(question)
            display_question(question)
        time.sleep(3)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    start_loop()
