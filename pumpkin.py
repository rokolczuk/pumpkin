__author__ = 'andrzej'
__author__ = 'andrzej'

import max7219.led as led
import pygame

pygame.mixer.init()

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
            #print(str(row) + "x" + str(col) + ": " + char)
            device.pixel(col, row, int(char), redraw=False)

    device.flush()

draw_matrix(test)
