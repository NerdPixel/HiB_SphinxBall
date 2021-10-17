import logging
import time

from mpu6050 import mpu6050
from time import sleep
from grove_rgb_lcd import *

import RPi.GPIO as GPIO


def test_vibration(vibrations):
    for i in range(10):
        logging.info("Vibrate!!!")
        GPIO.output(vibrations, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(vibrations, GPIO.LOW)
        time.sleep(0.2)


def test_sound(sound):
    pass


def test_gyro():
    sensor = mpu6050(0x68, bus=4)
    for i in range(10):
        accel_data = sensor.get_accel_data()
        gyro_data = sensor.get_gyro_data()
        temp = sensor.get_temp()

        print("Accelerometer data")
        print("x: " + str(accel_data['x']))
        print("y: " + str(accel_data['y']))
        print("z: " + str(accel_data['z']))

        print("Gyroscope data")
        print("x: " + str(gyro_data['x']))
        print("y: " + str(gyro_data['y']))
        print("z: " + str(gyro_data['z']))

        print("Temp: " + str(temp) + " C")
        sleep(1)


def test_display():
    setRGB(0, 255, 0)
    setText("Halli Hallo!!!")
    time.sleep(2)


if __name__ == '__main__':
    logging.basicConfig(filename='test_station.log', level=logging.INFO)
    vibrations = 37
    sound = 15

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(vibrations, GPIO.OUT)
    GPIO.setup(sound, GPIO.IN)

    # test_vibration(vibrations)
    # test_sound(sound)
    test_gyro()
    test_display()
    GPIO.cleanup()
