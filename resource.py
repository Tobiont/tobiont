"""A container representing an amount of a game resource or food."""

class Resource(object):
	"""Container for resources."""
	_type = ""
	_quantity = 0

	def __init__(self, type, quantity):
		self.type = type
		self.quantity = quantity

	def getResource(self):
		return self._quantity

	def getType(self):
		return self._type

	def addResource(self, quantity):
		self._quantity += quantity

	def subtractResource(self, quantity):
		self._quantity -= quantity

	def setType(self, resource_type):
		self._type = resource_type


