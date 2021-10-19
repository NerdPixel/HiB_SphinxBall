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

bus = smbus.SMBus(4)  # set bus for I2C
Device_Address = 0x68  # MPU6050 device address


def choose_random_question():
    data = json.load(open('example-questions.json'))
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
    print(" Reading Data of Gyroscope and Accelerometer")
    new_acc_data = get_gyro_data()
    logging.info(gyro_rest)
    logging.info(new_acc_data)
    logging.info(not np.allclose(gyro_rest, new_acc_data))
    return not np.allclose(gyro_rest, new_acc_data)


def display_question(question):
    LCD.setRGB(0, 255, 0)
    LCD.setText(question)


def start_loop():
    MPU_Init()
    while True:
        if gyro_changed():
            question = choose_random_question()
            logging.info(question)
            display_question(question)
        time.sleep(3)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    start_loop()
