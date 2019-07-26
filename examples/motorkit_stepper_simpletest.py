"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
import time

kit = MotorKit()

for i in range(100):
    kit.stepper1.onestep()
    time.sleep(0.01)
