from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='10.0.0.148', port=8889)
servoPIN = 12
servo = Servo(pin=servoPIN, pin_factory=factory)

try:
    while True:
        servo.min()
        sleep(2)
        servo.mid()
        sleep(2)
        servo.max()
except KeyboardInterrupt:
    servo.stop()