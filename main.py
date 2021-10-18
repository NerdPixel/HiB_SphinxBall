#!/usr/bin/env python3
import time
import logging
import json
from random import randrange
from mpu6050 import mpu6050
import LCD as LCD
import numpy as np

sensor = mpu6050(0x68, bus=4)
old_accel_data = sensor.get_accel_data(g=True)


def choose_random_question():
    data = json.load(open('example-questions.json'))
    return data[randrange(len(data))]["frage"]


def gyro_changed():
    try:
        accel_data = sensor.get_accel_data(g=True)
    except IOError as ioe:
        logging.error("Gyro wrong")
        logging.debug(ioe)
        return False
    global old_accel_data
    is_changed = np.allclose(old_accel_data, accel_data)
    old_accel_data = accel_data
    return is_changed


def display_question(question):
    LCD.setRGB(0, 255, 0)
    LCD.setText(question)


def start_loop():
    while True:
        if gyro_changed(sensor):
            question = choose_random_question()
            logging.info(question)
            display_question(question)
        time.sleep(3)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    start_loop()
