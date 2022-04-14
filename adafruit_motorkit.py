# SPDX-FileCopyrightText: 2017 Scott Shawcroft for Adafruit Industries
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_motorkit`
====================================================

CircuitPython helper library for DC & Stepper Motor FeatherWing, Shield, and Pi Hat kits.

* Author(s): Scott Shawcroft, Kattni Rembor

Implementation Notes
--------------------

**Hardware:**

* `DC Motor + Stepper FeatherWing <https://www.adafruit.com/product/2927>`_
* `Adafruit Motor/Stepper/Servo Shield for Arduino v2 Kit <https://www.adafruit.com/product/1438>`_
* `Adafruit DC & Stepper Motor HAT for Raspberry Pi - Mini Kit
  <https://www.adafruit.com/product/2348>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

 * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
 * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
 * Adafruit's PCA9685 library: https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
 * Adafruit's Motor library: https://github.com/adafruit/Adafruit_CircuitPython_Motor

"""

import board
from adafruit_pca9685 import PCA9685

try:
    from typing import Optional, Tuple
    from busio import I2C
    import adafruit_motor.motor
    import adafruit_motor.stepper
except ImportError:
    pass

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_MotorKit.git"


class MotorKit:
    """Class representing an Adafruit DC & Stepper Motor FeatherWing, Shield or Pi Hat kit.

    :param int address: I2C address of PCA9685 PWM controller. Default address is ``0x60``.
    :param busio.I2C i2c: I2C bus object to use. If not specified, use ``board.I2C()``.

      .. note::
        ``board.I2C()`` uses the default I2C bus frequency of 100 kHz. To speed up
        motor control, use an I2C bus frequency of 400 KHz, or if available, 1 MHz.
        The PCA9685 controller supports both of these higher speeds.
        This will noticeably speed up stepper motor operation when many steps are requested.

    :param int steppers_microsteps: Number of microsteps per step for stepper motors. Default is 16.
    :param float pwm_frequency: defaults to 1600 Hz
    """

    def __init__(
        self,
        address: int = 0x60,
        i2c: Optional[I2C] = None,
        steppers_microsteps: int = 16,
        pwm_frequency: float = 1600.0,
    ) -> None:
        self._motor1 = None
        self._motor2 = None
        self._motor3 = None
        self._motor4 = None
        self._stepper1 = None
        self._stepper2 = None
        if i2c is None:
            i2c = board.I2C()
        self._pca = PCA9685(i2c, address=address)
        self._pca.frequency = pwm_frequency
        self._steppers_microsteps = steppers_microsteps

    # We can save memory usage (~300 bytes) by deduplicating the construction of the objects for
    # each motor. This saves both code size and the number of raw strings (the error message)
    # stored. The same technique is a net loss for stepper because there is less duplication.
    def _motor(
        self, motor_name: int, channels: Tuple[int, int, int], stepper_name: int
    ) -> adafruit_motor.motor.DCMotor:
        from adafruit_motor import motor  # pylint: disable=import-outside-toplevel

        motor_name = "_motor" + str(motor_name)
        stepper_name = "_stepper" + str(stepper_name)
        if not getattr(self, motor_name):
            if getattr(self, stepper_name):
                raise RuntimeError(
                    "Cannot use {} at the same time as {}.".format(
                        motor_name[1:], stepper_name[1:]
                    )
                )
            self._pca.channels[channels[0]].duty_cycle = 0xFFFF
            setattr(
                self,
                motor_name,
                motor.DCMotor(
                    self._pca.channels[channels[1]], self._pca.channels[channels[2]]
                ),
            )
        return getattr(self, motor_name)

    @property
    def motor1(self) -> adafruit_motor.motor.DCMotor:
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
    def motor2(self) -> adafruit_motor.motor.DCMotor:
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
    def motor3(self) -> adafruit_motor.motor.DCMotor:
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
    def motor4(self) -> adafruit_motor.motor.DCMotor:
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
    def stepper1(self) -> adafruit_motor.stepper.StepperMotor:
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
            from adafruit_motor import (  # pylint: disable=import-outside-toplevel
                stepper,
            )

            if self._motor1 or self._motor2:
                raise RuntimeError(
                    "Cannot use stepper1 at the same time as motor1 or motor2."
                )
            self._pca.channels[8].duty_cycle = 0xFFFF
            self._pca.channels[13].duty_cycle = 0xFFFF
            self._stepper1 = stepper.StepperMotor(
                self._pca.channels[10],
                self._pca.channels[9],
                self._pca.channels[11],
                self._pca.channels[12],
                microsteps=self._steppers_microsteps,
            )
        return self._stepper1

    @property
    def stepper2(self) -> adafruit_motor.stepper.StepperMotor:
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
            from adafruit_motor import (  # pylint: disable=import-outside-toplevel
                stepper,
            )

            if self._motor3 or self._motor4:
                raise RuntimeError(
                    "Cannot use stepper2 at the same time as motor3 or motor4."
                )
            self._pca.channels[7].duty_cycle = 0xFFFF
            self._pca.channels[2].duty_cycle = 0xFFFF
            self._stepper2 = stepper.StepperMotor(
                self._pca.channels[4],
                self._pca.channels[3],
                self._pca.channels[5],
                self._pca.channels[6],
                microsteps=self._steppers_microsteps,
            )
        return self._stepper2

    @property
    def frequency(self) -> float:
        """The overall PCA9685 PWM frequency in Hertz."""
        return self._pca.frequency

    @frequency.setter
    def frequency(self, pwm_frequency: float = 1600.0) -> None:
        self._pca.frequency = pwm_frequency
