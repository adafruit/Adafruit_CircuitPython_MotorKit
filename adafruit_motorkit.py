# The MIT License (MIT)
#
# Copyright (c) 2017 Scott Shawcroft for Adafruit Industries
# Copyright (c) 2018 Kattni Rembor for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_motorkit`
====================================================

.. CircuitPython helper library for DC & Stepper Motor FeatherWing, Shield, and Pi Hat kits.

* Author(s): Scott Shawcroft, Kattni Rembor

Implementation Notes
--------------------

**Hardware:**

   "* `DC Motor + Stepper FeatherWing <https://www.adafruit.com/product/2927>`_"
   "* `Adafruit Motor/Stepper/Servo Shield for Arduino v2 Kit
   <https://www.adafruit.com/product/1438>`_"
   "* `Adafruit DC & Stepper Motor HAT for Raspberry Pi - Mini Kit
   <https://www.adafruit.com/product/2348>`_"

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

 * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
 * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
 * Adafruit's PCA9685 library: https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
 * Adafruit's Motor library: https://github.com/adafruit/Adafruit_CircuitPython_Motor

"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_MotorKit.git"

import board
import busio
from adafruit_pca9685 import PCA9685


class MotorKit:
    """Class representing an Adafruit DC & Stepper Motor FeatherWing, Shield or Pi Hat kit.

       Automatically uses the I2C bus on a Feather, Metro or Raspberry Pi."""
    def __init__(self, address=0x60):
        self._motor1 = None
        self._motor2 = None
        self._motor3 = None
        self._motor4 = None
        self._stepper1 = None
        self._stepper2 = None
        i2c = busio.I2C(board.SCL, board.SDA)
        self._pca = PCA9685(i2c, address=address)
        self._pca.frequency = 1600

    # We can save memory usage (~300 bytes) by deduplicating the construction of the objects for
    # each motor. This saves both code size and the number of raw strings (the error message)
    # stored. The same technique is a net loss for stepper because there is less duplication.
    def _motor(self, motor_name, channels, stepper_name):
        from adafruit_motor import motor
        motor_name = "_motor" + str(motor_name)
        stepper_name = "_stepper" + str(stepper_name)
        if not getattr(self, motor_name):
            if getattr(self, stepper_name):
                raise RuntimeError(
                    "Cannot use {} at the same time as {}.".format(motor_name[1:],
                                                                   stepper_name[1:]))
            self._pca.channels[channels[0]].duty_cycle = 0xffff
            setattr(self, motor_name, motor.DCMotor(self._pca.channels[channels[1]],
                                                    self._pca.channels[channels[2]]))
        return getattr(self, motor_name)

    @property
    def motor1(self):
        """:py:class:``~adafruit_motor.motor.DCMotor`` controls for motor 1.

            The following image shows the location of the M1 terminal on the DC/Stepper FeatherWing.
            The label on the FeatherWing is found on the bottom of the board.
            The terminal is labeled on the top of the Shield and Pi Hat.

            .. image :: ../docs/_static/motor_featherwing/m1.jpg
              :alt: Motor 1 location

            This example moves the motor forwards for one fifth of a second at full speed.

            .. code-block:: python

                import time
                from adafruit_motorkit import motorkit

                kit = MotorKit()

                kit.motor1.throttle = 1.0
                time.sleep(0.2)

                kit.motor1.throttle = 0
        """
        return self._motor(1, (8, 9, 10), 1)

    @property
    def motor2(self):
        """:py:class:``~adafruit_motor.motor.DCMotor`` controls for motor 2.

            The following image shows the location of the M2 terminal on the DC/Stepper FeatherWing.
            The label on the FeatherWing is found on the bottom of the board.
            The terminal is labeled on the top of the Shield and Pi Hat.

            .. image :: ../docs/_static/motor_featherwing/m2.jpg
              :alt: Motor 2 location

            This example moves the motor forwards for one fifth of a second at full speed.

            .. code-block:: python

                import time
                from adafruit_motorkit import motorkit

                kit = MotorKit()

                kit.motor2.throttle = 1.0
                time.sleep(0.2)

                kit.motor1.throttle = 0
        """
        return self._motor(2, (13, 11, 12), 1)

    @property
    def motor3(self):
        """:py:class:``~adafruit_motor.motor.DCMotor`` controls for motor 3.

            The following image shows the location of the M2 terminal on the DC/Stepper FeatherWing.
            The label on the FeatherWing is found on the bottom of the board.
            The terminal is labeled on the top of the Shield and Pi Hat.

            .. image :: ../docs/_static/motor_featherwing/m3.jpg
              :alt: Motor 3 location

            This example moves the motor forwards for one fifth of a second at full speed.

            .. code-block:: python

                import time
                from adafruit_motorkit import motorkit

                kit = MotorKit()

                kit.motor3.throttle = 1.0
                time.sleep(0.2)

                kit.motor1.throttle = 0
        """
        return self._motor(3, (2, 3, 4), 2)

    @property
    def motor4(self):
        """:py:class:``~adafruit_motor.motor.DCMotor`` controls for motor 4.

            .. image :: ../docs/_static/motor_featherwing/m4.jpg
              :alt: Motor 4 location

            This example moves the motor forwards for one fifth of a second at full speed.

            .. code-block:: python

                import time
                from adafruit_motorkit import motorkit

                kit = MotorKit()

                kit.motor4.throttle = 1.0
                time.sleep(0.2)

                kit.motor1.throttle = 0
        """
        return self._motor(4, (7, 5, 6), 2)

    @property
    def stepper1(self):
        """:py:class:``~adafruit_motor.stepper.StepperMotor`` controls for one connected to stepper
           1 (also labeled motor 1 and motor 2).

            The following image shows the location of the stepper1 terminals on the DC/Stepper
            FeatherWing. stepper1 is made up of the M1 and M2 terminals.
            The labels on the FeatherWing are found on the bottom of the board.
            The terminals are labeled on the top of the Shield and Pi Hat.

            .. image :: ../docs/_static/motor_featherwing/stepper1.jpg
              :alt: Stepper 1 location

            This example moves the stepper motor 100 steps forwards.

            .. code-block:: python

                from adafruit_motorkit import MotorKit

                kit = MotorKit()

                for i in range(100):
                    kit.stepper1.onestep()
        """
        if not self._stepper1:
            from adafruit_motor import stepper
            if self._motor1 or self._motor2:
                raise RuntimeError("Cannot use stepper1 at the same time as motor1 or motor2.")
            self._pca.channels[8].duty_cycle = 0xffff
            self._pca.channels[13].duty_cycle = 0xffff
            self._stepper1 = stepper.StepperMotor(self._pca.channels[10], self._pca.channels[9],
                                                  self._pca.channels[11], self._pca.channels[12])
        return self._stepper1

    @property
    def stepper2(self):
        """:py:class:``~adafruit_motor.stepper.StepperMotor`` controls for one connected to stepper
           2 (also labeled motor 3 and motor 4).

            The following image shows the location of the stepper2 terminals on the DC/Stepper
            FeatherWing. stepper2 is made up of the M3 and M4 terminals.
            The labels on the FeatherWing are found on the bottom of the board.
            The terminals are labeled on the top of the Shield and Pi Hat.

            .. image :: ../docs/_static/motor_featherwing/stepper2.jpg
              :alt: Stepper 2 location

            This example moves the stepper motor 100 steps forwards.

            .. code-block:: python

                from adafruit_motorkit import MotorKit

                kit = MotorKit()

                for i in range(100):
                    kit.stepper2.onestep()
        """
        if not self._stepper2:
            from adafruit_motor import stepper
            if self._motor3 or self._motor4:
                raise RuntimeError("Cannot use stepper2 at the same time as motor3 or motor4.")
            self._pca.channels[7].duty_cycle = 0xffff
            self._pca.channels[2].duty_cycle = 0xffff
            self._stepper2 = stepper.StepperMotor(self._pca.channels[4], self._pca.channels[3],
                                                  self._pca.channels[5], self._pca.channels[6])
        return self._stepper2
