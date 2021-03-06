"""These are universal static variables and settings."""

class Error(Exception):
  """Base Error class."""

class TransferError(Error):
  """A class of errors related to moving things between squares."""

class SquareOccupiedError(TransferError):
  """Failure to move a creature from one square to another."""

BOARD_X_SIZE = 20
BOARD_Y_SIZE = 20

DEMO_LENGTH_SECONDS = 60
DEMO_SPEED_SECONDS = .5