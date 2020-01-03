import random as random
import time as time
import machine as machine

#Define LED on Pin D6 of NodeMCU
pin = machine.Pin(2, machine.Pin.OUT)
#Set Power with modulation on pin
pwm = machine.PWM(pin)
#define the random period that the LED will stay ON
def muzika():
    for i in range(25):
     pwm.duty(random.getrandbits(10))
     pwm.freq(random.getrandbits(4))
     pin.on()
     time.sleep_ms(random.getrandbits(10))
     pin.off()


muzika()
