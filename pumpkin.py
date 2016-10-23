__author__ = 'andrzej'

import max7219.led as led
import pygame
from time import sleep

pygame.mixer.init()
pygame.mixer.music.set_volume(1)

test = [
    "0000000000000000",
    "0110000000000110",
    "1111100000011111",
    "0011110000111100",
    "0011111001111100",
    "0001111001111000",
    "0000000000000000",
    "0000000000000000"
]

device = led.matrix(cascaded=2)

def draw_matrix(matrix):
    for row, line_str in enumerate(matrix):
        for col, char in enumerate(line_str):
            device.pixel(col, row, int(char), redraw=False)

    device.flush()

def play_audio(path):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()


draw_matrix(test)
play_audio("laugh.mp3")

while True:
	sleep(1)
