#### EXERCISE LVL 1 ####

from machine import Pin
import utime

''' Pins for sensor '''
trigger = Pin(14, Pin.OUT) # GP14, pin 19
echo    = Pin(15, Pin.IN)  # GP15, pin 20

''' Pin for LED '''
led     = Pin(18, Pin.OUT) # GP18, pin 24

def main_function():
    trigger.low()                       # set low
    utime.sleep_us(2)                   # stay at the low setting for 2 micro seconds
    trigger.high()                      # set high
    utime.sleep_us(5)                   # stay at the high setting for 5 micro seconds
    trigger.low()                       # set low
   
    ''' Check to see if an echo has been received or not'''
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
       
    ''' Find out how much time has passed since we sent out the signal '''    
    timepassed = signalon - signaloff
   
    ''' Find out the distance that is between the sensor and the reflected surface '''
    distance = (timepassed * 0.0343) / 2  # Speed of sound in air = 342 m/s
   
    ''' Print the distance to the console for us to see'''
    print (0, "Distance (cm) :", distance, 30 )
    
    if (distance > 30):
        led.low()
    else:
        led.high() 

''' Cycle thorugh these instructions forever '''
if __name__ == '__main__':
    while True:
        main_function()           # execute the function we just wrote
        utime.sleep(0.5)          # time between sending reports to the console


