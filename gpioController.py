# import RPi.GPIO as GPIO
import time
class GPIO(object):

    def __init__(self):
        self.pin1 = 11 #p0
        self.pin2 = 12 #p5
        self.pin3 = 15 #p3
        self.pin4 = 13 #p4
        self.initGPIO()
        import RPi.GPIO as GPIO
        self.GPIO = GPIO

    def initGPIO(self):
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setup(self.pin1, GPIO.OUT)
        self.GPIO.setup(self.pin2, GPIO.OUT)
        self.GPIO.setup(self.pin3, GPIO.OUT)
        self.GPIO.setup(self.pin4, GPIO.OUT)

    def GoStraight(self,time):
        status = True
        while status:
            self.GPIO.output(PIN1, True)
            self.GPIO.output(PIN3, True)
            time.sleep(time)
            status = False
        self.GPIO.output(PIN1, False)
        self.GPIO.output(PIN3, False)
        return

    def TurnAround(self,rotate_time,rotate_way):
        if rotate_way == "Right":
            status = True
            while status:
                GPIO.output(PIN2, True)
                GPIO.output(PIN3, True)
                time.sleep(time)
                status = False
            self.GPIO.output(PIN2, False)
            self.GPIO.output(PIN3, False)
        else:
            status = True
            while status:
                GPIO.output(PIN1, True)
                GPIO.output(PIN4, True)
                time.sleep(rotate_time)
                status = False
            self.GPIO.output(PIN1, False)
            self.GPIO.output(PIN4, False)
        return
