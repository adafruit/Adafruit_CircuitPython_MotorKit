"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit

kit = MotorKit()

for i in range(100):
    kit.stepper1.onestep()
