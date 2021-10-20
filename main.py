#!/usr/bin/env python3
import time
import logging
import json
from random import randrange
import LCD as LCD
import smbus
import numpy as np

# some MPU6050 Registers and their Address
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47

# specify which file to load questions from, e.g. 'example-questions.json'
question_file = 'questions_final.json'

bus = smbus.SMBus(4)  # set bus for I2C
Device_Address = 0x68  # MPU6050 device address


# loads JSON file with questions as specified in question_file variable
# selects random question from the file and outputs its question string
def choose_random_question():
    logging.info("Loading questions from {}".format(question_file))
    data = json.load(open(question_file))
    return data[randrange(len(data))]["frage"]


def MPU_Init():
    # write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    # Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    # Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    # Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    # Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)


def read_raw_data(addr):
    # Accelero and Gyro value are 16-bit
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr + 1)

    # concatenate higher and lower value
    value = ((high << 8) | low)

    # to get signed value from mpu6050
    if (value > 32768):
        value = value - 65536
    return value


def get_gyro_data():
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)

    Ax = acc_x / 16384.0
    Ay = acc_y / 16384.0
    Az = acc_z / 16384.0
    return np.array([Ax, Ay, Az])


gyro_rest = get_gyro_data()


def gyro_changed():
    logging.info("Reading Data of Gyroscope and Accelerometer")
    new_acc_data = get_gyro_data()
    logging.info("gyro old:")
    logging.info(gyro_rest)
    logging.info("gyro new:")
    logging.info(new_acc_data)
    test = not np.allclose(gyro_rest, new_acc_data, atol=0.3)
    logging.info("gyro changed:")
    logging.info(test)
    return test


# put string into chunks of size size
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


# display question, while looping over the chunks of size 32
def display_question(question):
    LCD.setRGB(0, 0, 0)
    for chunk in chunker(question, 32):
        LCD.setText(chunk)
        time.sleep(3)

# loop to manage everything
def start_loop():
    MPU_Init()
    while True:
        if gyro_changed():
            question = choose_random_question()
            logging.info(question)
            display_question(question)
        time.sleep(0.5)


if __name__ == '__main__':
    # basic setup of the logger & start of the main loop
    logging.basicConfig(level=logging.DEBUG)
    start_loop()
