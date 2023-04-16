import sys
sys.path.append("../..")
from newsrc.kicad.board import *

class Board_test:
    def __init__(self, verbose=False):
        self.verbose = verbose

        board = Board()

        board.update()
        print(board)



Board_test(False)
