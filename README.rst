Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-motorkit/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/motorkit/en/latest/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_MotorKit/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_MotorKit/actions/
    :alt: Build Status

CircuitPython helper library for the DC & Stepper Motor FeatherWing, Shield and Pi Hat kits.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_
* `PCA9685 <https://github.com/adafruit/Adafruit_CircuitPython_PCA9685>`_
* `Motor <https://github.com/adafruit/Adafruit_CircuitPython_Motor>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
--------------------

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-motorkit/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-motorkit

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-motorkit

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-motorkit

Usage Example
=============

DC motor example:

.. code-block:: python

    import time
    from adafruit_motorkit import MotorKit

    kit = MotorKit()

    kit.motor1.throttle = 1.0
    time.sleep(0.5)
    kit.motor1.throttle = 0

Stepper motor example:

.. code-block:: python

    import time
    from adafruit_motorkit import MotorKit

    kit = MotorKit()

    for i in range(100):
        kit.stepper1.onestep()

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/motorkit/en/latest/>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_MotorKit/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
