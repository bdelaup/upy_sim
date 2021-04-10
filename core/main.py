from configuration import ConfigureForR2
ConfigureForR2.run()

from machine import Pin
from time import sleep


p1 = Pin(1, Pin.OUT)
p2 = Pin(2, Pin.OUT)

for i in range(2):
    p1.off()
    sleep(1)
    p1.on()
    p2.on()
    sleep(1)
    p2.off()
    sleep(1)

    
    

