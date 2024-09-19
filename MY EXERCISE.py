#### Iona's EXERCISE
from   machine import Pin, PWM
from   time    import sleep
import utime   as clocktool

''' Pins for sensor '''
trigger = Pin(3, Pin.OUT)   # this pin sends out information
echo    = Pin(2, Pin.IN)    # this pin takes in information

''' Pin for On-board LED '''
led = Pin(25, Pin.OUT)
pwm = PWM(Pin(15))
pwm.freq(1000)

'''PWM Info'''
duty = 0
maxDuty = 65025
maxDist = 5

''' Main method for sensor '''
def main_function():
    
   ''' Turn on LED'''
   led.high()                          # this lets us know the main function has been accessed

   '''Create a sin wave on the Trigger pin'''
   triggerON = clocktool.ticks_us()    # find out the time that this line was executed
   trigger.low()                       # switch off 
   clocktool.sleep_us(10)              # remain at this state for 10 micro seconds
   trigger.high()                      # switch on
   clocktool.sleep_us(10)              # remain at this state for 10 micro seconds
   trigger.low()                       # switch off 
   triggerOFF = clocktool.ticks_us()   # find out the time that this step was executed
   
   duration  = triggerOFF-triggerON    # this will let us know the time taekn to complete our square wave
   
   signalOFF = triggerOFF              # take a copy of the time that the signal was turned off
   signalON  = triggerOFF              # this number is saved into 2 locations as a starting point for other measurements

   while ( (echo.value() == 0) and (clocktool.ticks_diff(clocktool.ticks_us(), triggerOFF) < 25000) ): # if an echo is not being received for a duration of 
      signalOFF = clocktool.ticks_us()
   
   while ( (echo.value() == 1) and (clocktool.ticks_diff(clocktool.ticks_us(), signalOFF) < 25000) ):
      signalON = clocktool.ticks_us()
   
   ''' Get the time between signal sent and received '''
   timepassed = clocktool.ticks_diff(signalON, signalOFF)

   ''' Calculate the distance '''
   distance = (timepassed * 0.0343) / 2

   ''' Turn LED off '''
   led.low()

   ''' Show the answer on the screen '''
   print("The distance from object is ", distance, "cm")

   
   if distance < maxDist :
       percentage = (distance / maxDist) / 100
       print (percentage)
       
       duty = percentage * maxDist
        
   elif distance >= maxDist:
       duty = maxDuty

   if duty >= 0:
       pwm.duty_u16(int(duty))

try:
   ''' Repeat code in a loop'''
   while True:
      ''' Turn sensors switch on high '''

      ''' Look for objects '''
      main_function()
      
      ''' Stop code for a second so it doesnt miss anything '''
      clocktool.sleep(0.5)

finally:
   ''' When code is turned off, switch everything off '''
   vcc.low()
   trigger.low()
   led.low()
