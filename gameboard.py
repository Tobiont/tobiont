import globals
import resource
import weather

class Gameboard(object):
	"""Manages the gameboard representing the simulation world."""

	_board = []

	def __init__(self):
		super(Gameboard, self).__init__()

	for x in range(0, globals.BOARD_X_SIZE):
		for y in range(0, globals.BOARD_Y_SIZE):
			_board[x][y] = self._createGameSquare()

	def _createGameSquare(self):
		weather = RaineyWeather('defaultRegion', 'RaineyBiome')
		return GameAquare(resource.Resource('basic', 1), weather)

	def getSquare(self, x, y):
		return self._board[x][y]

class GameSquare(object):
	"""A single location square in the gameboard."""

	_resources = {}
	_contents = None
	_observers = []
	_weather_rules = None

	def __init__(self, resources, weather):
		super(Gamesquare, self).__init__()

		self._resources.update(resources)
		self._weather_rules = weather

    def moveCreatureToSquare(self, creature):
    	"""Adds a creature to this square or throws SquareOccupiedError."""
    	self._contents = creature

    def withdrawResource(self, resource):
    	"""Removes a resource from the square and returns it."""
    	if resource.getResource() = 0:
    		return
    	else:
    		self._resources[resource.getType()] == resource.getResource()

    def addResource(self, resource):
    	"""Adds a resource to this square."""
    	if resource.getResource() = 0:
    		return
    	else:
    		self._resources[resource.getType()] += resource.getResource()

 	def processWeather(self):
 		"""Runs the weather rules of the square."""
 		self._weather_rules.run(self)

 	def changeWeather(self, new_weather_rules):
 		"""Sets new weather rules."""
 		self._weather_rules = new_weather_rules

 	def registerObserver(self, observer):
 		"""Adds an observer to this square.

 		observers will be notified of actions taken by this square.
 		"""
 		self._observers.append(observer)

 	def removeObserver(self, observer):
 		"""Removes a registered observer."""
 		self._observers.remove(observer)

    def _alertObservers(self, message):
    	"""Internal alert method."""
    	for observer in self._observers:
    		observer.alert(message)