class Coordinate(tuple):
	"""Defines a Cartesian coordinate as a tuple of length 2.

	>>> coord = Coordinate(1, 2)
	>>> coord.x
	1
	>>> coord.y
	2
	>>> print coord
	(1, 2)

	"""
	
	def __new__(cls, x=0, y=0):
		"""
		@param x: The x-coordinate
		@param y: The y-coordinate

		"""
		
		return tuple.__new__(cls, (x, y))
		
	@property
	def x(self):
		"""Returns the x-coordinate - the first item of the tuple."""

		return self[0]
	
	@property
	def y(self):
		"""Returns the y-coordinate - the second item of the tuple."""

		return self[1]