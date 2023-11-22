from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

pigpio_factory = PiGPIOFactory()
servo1 = Servo(24 , pin_factory=pigpio_factory)
servo2 = Servo(25 , pin_factory=pigpio_factory)

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
