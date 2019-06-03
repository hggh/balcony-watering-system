#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import argparse

GPIO.setmode(GPIO.BCM)

def cleanup():
    GPIO.cleanup()

class Relay(object):
    gpio_pin = None

    def __init__(self, pin):
        self.gpio_pin = pin
        self._setup()

    def on(self):
        GPIO.output(self.gpio_pin, True)

    def off(self):
        GPIO.output(self.gpio_pin, False)

    def _setup(self):
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial=False)


class WaterLeverSensor(object):
    gpio_pin = None

    def __init__(self, pin):
        self.gpio_pin = pin

        self._setup()

    def water_available(self):
        # sensor needs to be connected to GPIO and 3.3V
        # if sensor is closed HIGH is on GPIO = water no longer available
        if int(GPIO.input(self.gpio_pin)) == 1:
            return False

        if int(GPIO.input(self.gpio_pin)) == 0:
            return True

        return None

    def _setup(self):
        GPIO.setup(self.gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def start_watering(run_time):
    r1.on()
    for i in range(run_time):
        time.sleep(1)
        if w1.water_available() is False:
            print("no longer water available")
            r1.off()
            break

    r1.off()

def water_status():
    if w1.water_available() is True:
        print("Water available")
    elif w1.water_available() is False:
        print("no Water available")

parser = argparse.ArgumentParser(description='Raspberry PI watering system')
parser.add_argument('--time', type=int, default=60, help='time in seconds')
parser.add_argument('--watering', default=False, action='store_true', help='start watering')
parser.add_argument('--water-status', default=False, action='store_true', help='check water level sensor and exit')
args = parser.parse_args()

w1 = WaterLeverSensor(pin=4)
r1 = Relay(pin=17)

if w1.water_available() is False:
    print("no water available")
    cleanup()
    exit()

try:
    if args.watering is True:
        start_watering(args.time)
    if args.water_status is True:
        water_status()
except Exception as e:
    print(e)
finally:
    cleanup()

