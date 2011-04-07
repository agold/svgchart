class Coordinate(tuple):
	"""Defines a Cartesian coordinate as a tuple of length 2."""
	
	def __new__(cls, x=0, y=0):
			return tuple.__new__(cls, (x, y))
		
	@property
	def x(self):
		return self[0]
	
	@property
	def y(self):
		return self[1]