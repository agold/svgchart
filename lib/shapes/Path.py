from Coordinate import Coordinate

class Path(object):
	"""Defines a path from a tuple of Coordinates."""
	coordinates = ()
	
	def __init__(self, coordinates=()):
		if isinstance(coordinates, tuple):
			for coord in coordinates:
				if not isinstance(coord, Coordinate):
					raise TypeError("Coordinates must be of type 'Coordinate'")
			self.coordinates = coordinates
		else:
			raise TypeError("coordinates must be a tuple")