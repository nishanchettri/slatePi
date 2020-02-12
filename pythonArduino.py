
import serial
import time
import sys
import os
import subprocess
from subprocess import*

movie1 = ("/home/pi/py532lib/1.mp4")
movie2 = ("/home/pi/py532lib/2.mp4")
#movie3 = ("/home/pi/sss5/vid3.mp4")

ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600

#myprocess = subprocess.Popen(['omxplayer','-b','/home/pi/py532lib/1.mp4'],stdin=subprocess.PIPE)

while(1):
    data=ser.read()
    if data == "a":
   #     myprocess.stdin.write('q')
    #    myprocess=subprocess.Popen(['omxplayer --adev hdmi','-b','/home/pi/py532lib/1.mp4'],stdin=subprocess.PIPE)
        os.system('killall omxplayer.bin')
        omxc = Popen(['omxplayer','-p','-b',movie1])

    elif data == "b":
        #myprocess.stdin.write('q')
        #myprocess=subprocess.Popen(['omxplayer ','-b','/home/pi/py532lib/2.mp4'],stdin=subprocess.PIPE)
        os.system('killall omxplayer.bin')
        omxc = Popen(['omxplayer','-p','-b',movie2])

