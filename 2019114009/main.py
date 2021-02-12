from input import *
import os
import board

if __name__ == "__main__":
    obj1 = Get()
    while(1):
        val = input_to(obj1)

        sys.stdout.write("\033c")
        # print(val)
        if val == 'q':
            break
        main_board = board.Board()
        main_board.render()