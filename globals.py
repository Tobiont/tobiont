"""These are universal static variables and settings."""

class Error(Exception):
  """Base Error class."""

class TransferError(Error):
  """A class of errors related to moving things between squares."""

class SquareOccupiedError(TransferError):
  """Failure to move a creature from one square to another."""

BOARD_X_SIZE = 10
BOARD_Y_SIZE = 10

DEMO_LENGTH_SECONDS = 2
DEMO_SPEED_SECONDS = 1