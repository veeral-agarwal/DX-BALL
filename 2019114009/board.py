import config
import random
from colorama import init, Fore, Back, Style
import numpy as np
# import global_var

class Board():

    height = int(config.rows)
    length = int(config.columns)

    def __init__(self):
        self.matrix = np.array([[ " " for i in range(self.length)] for j in range(self.height) ])
        self.upperborder()
        self.lowerborder()

    def render(self):
        for y in range( self.height):
            lol = []
            for x in range( 0 , config.columns):
                lol.append(self.matrix[y][x])
            print(''.join(lol))

    def upperborder(self):
        for x in range(self.length):
            self.matrix[3][x] = "X"

    def lowerborder(self):
        for x in range(self.length):
            self.matrix[39][x] = "="