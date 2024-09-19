#### US EXERCISE, Iona's Version ####

from machine import Pin, PWM
import utime


''' Pins for HC-SR04 sensor '''
trigger = Pin(14, Pin.OUT)     # GPIO 14, pin 19
echo    = Pin(15, Pin.IN)      # GPIO 15, pin 20

''' Pin for RPi's On-board LED '''
led     = Pin(25, Pin.OUT)

''' Pin for Piezo '''
piezo   = Pin(18, Pin.OUT)    # GPIO 18, pin 24


def main_function():
# indent here to show that this code lives within this function

       trigger.low()                       # set low
       utime.sleep_us(2)                   # stay at the low setting for 2 micro seconds
       trigger.high()                      # set high
       utime.sleep_us(5)                   # stay at the high setting for 5 micro seconds
       trigger.low()                       # set low
       
       ''' Check to see if an echo has been received or not'''
       while echo.value() == 0:            # when no echo has been heard yet
           signaloff = utime.ticks_us()    # check the time
       while echo.value() == 1:            # when an echo has been heard
           signalon = utime.ticks_us()     # check the time
           
       ''' Find out how much time has passed since we sent out the signal '''    
       timepassed = signalon - signaloff   # calculate the difference
       
       ''' Find out the distance that is between the sensor and the reflected surface '''
       # Speed of sound in air = 342 m/s OR 0.0343 cm/s
       distance = (timepassed * 0.0343) / 2       
       
       ''' Print the distance to the console for us to see'''
       print (0, "Distance (cm) :", distance, 30 )
       
       ''' Getting too close '''
       if distance >30:
           led.high()                      # switch on a light
           piezo.high()                    # switch on alarm ***** TO IMPLEMENT *****
           
       ''' Safe distance '''
       else:
           led.low()                       # switch off a light
           piezo.low()                     # witch off alarm

# code returning to the far left indicates that the function definition is complete


''' Cycle thorugh these instructions forever !!! '''
while True:
       main_function()                   # go to the function we just wrote and execute that behaviour
       utime.sleep(0.02)                 # sleep / "do nothing" for 0.02 seconds
                                         # the sleep duration dictates how frequently we want to check the distance and report back to the console

