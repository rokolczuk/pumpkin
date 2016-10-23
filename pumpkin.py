__author__ = 'andrzej'
__author__ = 'andrzej'

import max7219.led as led
import pygame

pygame.mixer.init()

test = [
    "10000000",
    "11000000",
    "11100000",
    "11110000",
    "11111000",
    "11111100",
    "11111110",
    "11111111"
]

device = led.matrix(cascaded=1)
device.pixel(0, 0, 2)

def draw_matrix(matrix):
    for row, line_str in enumerate(matrix):
        for col, char in enumerate(line_str):
            #print(str(row) + "x" + str(col) + ": " + char)
            device.pixel(col, row, int(char), redraw=False)

    device.flush()

draw_matrix(test)