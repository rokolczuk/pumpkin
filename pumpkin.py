__author__ = 'andrzej'
__author__ = 'andrzej'

import max7219.led as led
import pygame

pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 1, 2048)
pygame.mixer.music.set_volume(1)

test = [
    "1000000011111111",
    "1100000011111111",
    "1110000011111111",
    "1111000011100111",
    "1111100011111111",
    "1111110011111111",
    "1111111011111111",
    "1111111111111111"
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