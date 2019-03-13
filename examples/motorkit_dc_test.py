import time
from adafruit_motorkit import MotorKit

kit = MotorKit()

kit.motor1.throttle = 0

while True:
    print("Forward!")
    kit.motor1.throttle = 0.5
    time.sleep(1)

    print("Speed up...")
    for i in range(0, 101):
        speed = i * 0.01
        kit.motor1.throttle = speed
        time.sleep(0.01)

    print("Slow down...")
    for i in range(100, -1, -1):
        speed = i * 0.01
        kit.motor1.throttle = speed
        time.sleep(0.01)

    print("Backward!")
    kit.motor1.throttle = -0.5
    time.sleep(1)

    print("Speed up...")
    for i in range(0, -101, -1):
        speed = i * 0.01
        kit.motor1.throttle = speed
        time.sleep(0.01)

    print("Slow down...")
    for i in range(-100, 1):
        speed = i * 0.01
        kit.motor1.throttle = speed
        time.sleep(0.01)

    print("Stop!")
    kit.motor1.throttle = 0
    time.sleep(1)
