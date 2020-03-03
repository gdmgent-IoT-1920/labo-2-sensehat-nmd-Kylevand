from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

randomCol = (randint(0,255),randint(0,255),randint(0,255))
randomCol2 = (randint(0,255),randint(0,255),randint(0,255))
randomCol3 = (randint(0,255),randint(0,255),randint(0,255))

while True:
       
        sense.show_letter("N", text_colour=randomCol)
        time.sleep(1)
        sense.show_letter("M", text_colour=randomCol2)
        time.sleep(1)
        sense.show_letter("D", text_colour=randomCol3)
        time.sleep(3)