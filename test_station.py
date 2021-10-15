import logging
import time

from mpu6050 import mpu6050
import Adafruit_ADS1x15
import RPi.GPIO as GPIO


def test_vibration(vibrations):
    for i in range(10):
        logging.info("Vibrate!!!")
        GPIO.output(vibrations, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(vibrations, GPIO.LOW)
        time.sleep(0.2)


def test_sound(sound):
    ADS1115 = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    print('MAX9814 Microphone Module test script')
    print('[Press CTRL + C to end the script!]')
    try:
        while True:
            analog = ADS1115.read_adc(0, gain=GAIN)
    print('Analog: {}'.format(analog))
    time.sleep(0.002)
    except KeyboardInterrupt:
        print('\nScript end!')
    finally:
        GPIO.cleanup()

def test_gyro():
    sensor = mpu6050(0x68)
    for i in range(10):
        accelerometer_data = sensor.get_accel_data()
        logging.info(accelerometer_data)

if __name__ == '__main__':
    logging.basicConfig(filename='test_station.log', level=logging.INFO)
    vibrations = 37
    sound = 15

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(vibrations, GPIO.OUT)
    GPIO.setup(sound, GPIO.IN)

    #test_vibration(vibrations)
    #test_sound(sound)
    test_gyro()
    GPIO.cleanup()

