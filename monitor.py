from tobiont import globals
from tobiont import resource
from tobiont import weather

class Monitor(object):
    """Class to render gameboards in readable form."""

    def __init__(self):
        super(Monitor, self).__init__()
    def render(self, gameboard):
        #TODO: render gameboard

    def getPopulation(self, gameboard):
        population = 0
        for x in range(0, globals.BOARD_X_SIZE):
            for y in range(0, globals.BOARD_Y_SIZE):
                gameboard.getSquare(x, y) #TODO: analyze population of each square and add it to population
        return population
        
