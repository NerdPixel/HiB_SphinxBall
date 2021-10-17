#!/usr/bin/env python3
import time
import logging
import json
from random import randrange
from mpu6050 import mpu6050


def choose_random_question():
    data = json.load(open('example-questions.json'))
    return data[randrange(len(data))]["frage"]


def gyro_changed(sensor):
    try:
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()
        temp = sensor.get_temp()
    except IOError as ioe:
        logging.error("Gyro wrong")
        return False

    print("Accelerometer data")
    print("x: " + str(accel_data['x']))
    print("y: " + str(accel_data['y']))
    print("z: " + str(accel_data['z']))

    print("Gyroscope data")
    print("x: " + str(gyro_data['x']))
    print("y: " + str(gyro_data['y']))
    print("z: " + str(gyro_data['z']))

    print("Temp: " + str(temp) + " C")
    return True


def display_question(question):
    pass


def start_loop():
    sensor = mpu6050(0x68, bus=4)
    while True:
        if gyro_changed(sensor):
            question = choose_random_question()
            logging.info(question)
            display_question(question)
        time.sleep(1)


if __name__ == '__main__':
    logging.basicConfig(filename="sphinxBall.log", level=logging.DEBUG)
    start_loop()
