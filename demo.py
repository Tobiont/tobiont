import os
import time

from tobiont import gameboard
from tobiont import globals


def main():
  board = gameboard.Gameboard()

  for iteration in range(
      int(globals.DEMO_LENGTH_SECONDS / globals.DEMO_SPEED_SECONDS)):
    os.system('cls')
    print ("Time: %d seconds" % int(iteration * globals.DEMO_SPEED_SECONDS))
    board.processGameboard()
    printBoard(board)
    time.sleep(globals.DEMO_SPEED_SECONDS)


def printBoard(board):
  """Iterates through the gameboard and prints the resources in each square."""
  
  for y in range(0, globals.BOARD_Y_SIZE):
    line_buf = []
    for x in range(0, globals.BOARD_X_SIZE):
      sq = board.getSquare(x, y)
      line_buf.append(str(sq.getResource('basic')))
    print (''.join(line_buf))


if __name__ == "__main__":
    main()