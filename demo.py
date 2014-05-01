import os
import time

from tobiont import gameboard
from tobiont import globals


def run():
  board = gameboard.Gameboard()

  for iteration in range(1,
      int(globals.DEMO_LENGTH_SECONDS / globals.DEMO_SPEED_SECONDS) + 2):
    os.system('cls')
    print("Resources accumulated in each game square")
    print ("Elapsed: %d seconds" % int(iteration * globals.DEMO_SPEED_SECONDS))
    board.processGameboard()
    printBoard(board)
    time.sleep(globals.DEMO_SPEED_SECONDS)


def printBoard(board):
  """Iterates through the gameboard and prints the resources in each square."""
  
  for y in range(0, globals.BOARD_Y_SIZE):
    for x in range(0, globals.BOARD_X_SIZE):
      sq = board.getSquare(x, y)
      print(str(sq.getResource('basic')).ljust(3), end='')
    print ('')


if __name__ == "__main__":
    run()