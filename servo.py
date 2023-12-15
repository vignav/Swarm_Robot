from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
import math

pigpio_factory = PiGPIOFactory()
servo1 = Servo(24 , pin_factory=pigpio_factory)
servo2 = Servo(25 , pin_factory=pigpio_factory)

def servo1_set( value ):
    if abs(value) <= 1 :
        servo1.value = value
    else:
        servo1.value = 1

def servo2_set( value ):
    if abs(value) <= 1:
        servo2.value = value*-1
    else:
        servo2.value = 1

def go_dir ( value ):
    servo1_set(0.5+(value*0.5/math.pi))
    servo2_set(0.5-(value*0.5/math.pi))

def point_dir ( value ):
    servo1_set(value)
    servo2_set(value*-1)

if __name__ == '__main__' :
    try:
        while True:
            for i in range(-100,100,1):
                servo1.value = i/100
                servo2.value = i/100
                sleep(0.1)

    except KeyboardInterrupt:
        servo1.value = 0
        servo2.value = 0
        print("Program stopped")
