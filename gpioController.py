import RPi.GPIO as GPIO
import time
class GPIO(object):

    def __init__(self):
        self.pin1 = 11 #p0
        self.pin2 = 12 #p5
        self.pin3 = 13 #p3
        self.pin3 = 15 #p4
        self.initGPIO()

    def initGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin3, GPIO.OUT)
        GPIO.setup(self.pin4, GPIO.OUT)

    def GoStraight(self,time):
        status = True
        while status:
            GPIO.output(PIN1, True)
            GPIO.output(PIN3, True)
            time.sleep(time)
            status = False
        GPIO.output(PIN1, False)
        GPIO.output(PIN3, False)
        return

    def TurnAround(self,rotate_time,rotate_way):
        if rotate_way == "Right":
            status = True
            while status:
                GPIO.output(PIN2, True)
                GPIO.output(PIN3, True)
                time.sleep(time)
                status = False
            GPIO.output(PIN2, False)
            GPIO.output(PIN3, False)
        else:
            status = True
            while status:
                GPIO.output(PIN1, True)
                GPIO.output(PIN4, True)
                time.sleep(rotate_time)
                status = False
            GPIO.output(PIN1, False)
            GPIO.output(PIN4, False)
        return
