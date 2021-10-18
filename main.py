#!/usr/bin/env python3
import time
import logging
import json
from random import randrange
from mpu6050 import mpu6050
import LCD as LCD


def choose_random_question():
    data = json.load(open('example-questions.json'))
    return data[randrange(len(data))]["frage"]


def gyro_changed(sensor):
    try:
        accel_data = sensor.get_accel_data(g=True)
    except IOError as ioe:
        logging.error("Gyro wrong")
        return False
    print("Accelerometer data")
    print("x: " + str(accel_data['x']))
    print("y: " + str(accel_data['y']))
    print("z: " + str(accel_data['z']))

    return True


def display_question(question):
    LCD.setRGB(0, 255, 0)
    LCD.setText(question)


def start_loop():
    sensor = mpu6050(0x68, bus=4)
    while True:
        if gyro_changed(sensor):
            question = choose_random_question()
            logging.info(question)
            display_question(question)
        time.sleep(3)


if __name__ == '__main__':
    logging.basicConfig(filename="sphinxBall.log", level=logging.DEBUG)
    start_loop()
