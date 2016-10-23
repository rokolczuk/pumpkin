__author__ = 'andrzej'

import max7219.led as led
import pygame
from time import sleep

pygame.mixer.init()
pygame.mixer.music.set_volume(1)

eyes_open = [
    "0000000000000000",
    "0110000000000110",
    "1111100000011111",
    "0011110000111100",
    "0011111001111100",
    "0001111001111000",
    "0000000000000000",
    "0000000000000000"
]

eyes_opening = [

    "0000000000000000",
    "0000000000000000",
    "0111100000011110",
    "0011110000111100",
    "0001111001111000",
    "0000000000000000",
    "0000000000000000",
    "0000000000000000"
]

eyes_closed = [

    "0000000000000000",
    "0000000000000000",
    "0000000000000000",
    "0011110000111100",
    "0001100000011000",
    "0000000000000000",
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

def open_eyes():

    print("open eyes")
    draw_matrix(eyes_closed)
    sleep(0.3)
    draw_matrix(eyes_opening)
    sleep(0.3)
    draw_matrix(eyes_open)

def close_eyes():
    print("close eyes")
    draw_matrix(eyes_open)
    sleep(0.3)
    draw_matrix(eyes_opening)
    sleep(0.3)
    draw_matrix(eyes_closed)

while True:
    open_eyes()
    sleep(5)
    close_eyes()
    sleep(5)
