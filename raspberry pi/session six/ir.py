import RPi.GPIO as GPIO
import time
sensor_input = 16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.IN)
GPIO.setup(14,GPIO.OUT)
while True:
    x = GPIO.input(sensor_input)
    print("IR SIGNAL : ",x)
    if x == 1 :
        print ("led on")
        GPIO.output(14,GPIO.HIGH)
    else:
        print ("led off")
        GPIO.output(14,GPIO.LOW)
