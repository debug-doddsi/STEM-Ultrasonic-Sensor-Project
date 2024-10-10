#### EXERCISE LVL 2 ####

from machine import Pin
import utime

''' Pins for sensor '''
trigger = Pin(14, Pin.OUT)             # GP14, pin 19
echo    = Pin(15, Pin.IN)              # GP15, pin 20

''' Pin for Piezo'''
piezo   = Pin(19, Pin.OUT)             # GP19, pin 25

''' Pin for LED '''
led     = Pin(18, Pin.OUT) 	           # GP18, pin 24

def main_function():
    trigger.low()                      # set low
    utime.sleep_us(2)                  # stay at the low setting for 2 micro seconds
    trigger.high()                     # set high
    utime.sleep_us(5)                  # stay at the high setting for 5 micro seconds
    trigger.low()                      # set low
   
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

    if (distance > 30):                   # when an object is a safe distance away
        led.low()                         # do nothing
    else:                                 # when an object is too close
        for i in range(5):                # cycle through this part 5 times
            led.toggle()                  # flash the led
            piezo.toggle()                # beep the piezo
            utime.sleep_ms(100)           # wait for 100ms before beeping/flashing again
            i = i+1


''' Cycle through these instructions forever '''
while True:
    main_function()      # execute the main function
    utime.sleep(0.02)    # how often we want to check the distance 
 