#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

WATER_TIME = 10


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
        if GPIO.input(self.gpio_pin) == GPIO.HIGH:
            return False

        return True

    def _setup(self):
        GPIO.setup(self.gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

w1 = WaterLeverSensor(pin=17)
r1 = Relay(pin=4)
r1.on()

time.sleep(5)

r1.off()


print(w1.water_available())
print("Sleep")
time.sleep(5)
print(w1.water_available())

GPIO.cleanup()