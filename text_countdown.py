from sense_emu import SenseHat
from time import sleep
G =  [0, 255, 0]
sense_emulator = SenseHat()

i = 10
while i > 0:
    G[0]= G[0]+25
    i = i-1
    sleep(1)
    sense_emulator.show_letter(f"{i}",G)
    if i == 0:
        G =  [200, 0, 200]
        sense_emulator.show_letter(f"{i}",G)
