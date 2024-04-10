from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

s = 10
sleep(s)

a=0
b=0

timer = list[a,b]


sense.set_pixels(timer)

G = [0, 255, 0]
R = [255, 0, 0]
X = [0, 0, 0]

sense.set_pixels(G)

for i in range (0,s):
    sense.clear()
    sleep(0.1)
    sense.set_pixel(timer,G)
    sleep(0.1)