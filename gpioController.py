import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)


class GPIO(object):

    def __init__(self):
        self.pin1 = 11 #p0
        self.pin2 = 12 #p5
        self.pin3 = 15 #p3
        self.pin4 = 13 #p4
        self.GPIO = self.initGPIO()

    def initGPIO(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin3, GPIO.OUT)
        GPIO.setup(self.pin4, GPIO.OUT)
        return GPIO

    def GoStraight(self,time):
        status = True
        while status:
            self.GPIO.output(self.pin1, True)
            self.GPIO.output(self.pin4, True)
            time.sleep(time)
            status = False
        self.GPIO.output(self.pin1, False)
        self.GPIO.output(self.pin4, False)
        return

    def TurnAround(self,rotate_time,rotate_way):
        if rotate_way == "Right":
            status = True
            while status:
                GPIO = self.GPIO
                GPIO.output(self.pin2, True)
                GPIO.output(self.pin3, True)
                time.sleep(time)
                status = False
            GPIO = self.GPIO
            GPIO.output(self.pin2, False)
            GPIO.output(self.pin3, False)
        else:
            status = True
            while status:
                GPIO = self.GPIO
                GPIO.output(PIN1, True)
                GPIO.output(PIN4, True)
                time.sleep(rotate_time)
                status = False
            GPIO = self.GPIO
            GPIO.output(PIN1, False)
            GPIO.output(PIN4, False)
        return
