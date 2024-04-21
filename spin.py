from sr_ram import *

xz = 0
while True:
    xz = (xz+1) % 4096
    write("p1Data",pXZ,xz)
    write("p2Data",pXZ,xz)
    write("p3Data",pXZ,xz)
    write("p4Data",pXZ,xz)
    write("p5Data",pXZ,xz)
