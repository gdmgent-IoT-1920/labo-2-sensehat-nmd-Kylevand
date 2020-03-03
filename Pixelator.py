from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

vertical = 0
horizontal = 0

def randomCol():
	return (randint(0, 255), randint(0, 255), randint(0, 255))
    
while True:
	for vertical in range(8):
		for horizontal in range(8):
			sleep(0.5)
			sense.set_pixel(vertical, horizontal, randomCol())