import RPi.GPIO as GPIO
import time

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 14 for PWM with 50Hz
p.start(2) # Initialization
try:
  while True:
      for i in range(2,12,2):
              p.ChangeDutyCycle(i)
              time.sleep(0.5)
      for i in range(12,2,-2):
          p.ChangeDutyCycle(i)
          time.sleep(0.5)
              
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()