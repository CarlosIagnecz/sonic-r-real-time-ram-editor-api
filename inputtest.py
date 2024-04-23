from sr_ram import *
from time import sleep
from math import cos,sin,pi

spd = 4294967295 *10

while True:

    if plrInputTest(1,"Foward"):
        write("p1Data",pMomentum,spd)
    else:
        write("p1Data",pMomentum,0)
    sleep(0.1)
