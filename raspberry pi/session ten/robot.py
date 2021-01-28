# import curses, GPIO and time
import curses
import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(16,False)
                GPIO.output(18,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(16,True)
                GPIO.output(18,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(16,False)
                GPIO.output(18,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == curses.KEY_LEFT:
                GPIO.output(16,True)
                GPIO.output(18,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == ord('d'):
                GPIO.output(18,True)
                GPIO.output(15,True)
                time.sleep(.5)
                GPIO.output(16,True)
                GPIO.output(18,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
                time.sleep(.5)
                GPIO.output(16,True)
                GPIO.output(18,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
                time.sleep(.5)
                GPIO.output(16,False)
                GPIO.output(18,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
                time.sleep(.5)
                GPIO.output(18,False)
                GPIO.output(13,False)
            elif char == ord('s'):
                GPIO.output(16,False)
                GPIO.output(18,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
