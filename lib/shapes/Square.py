from Coordinate import Coordinate
from Rectangle import Rectangle

class Square(Rectangle):
	"""Defines a square as a rectangle with equal height and width."""

	def __init__(self, position=Coordinate(), size=0):
		if isinstance(position, Coordinate):
			Rectangle.__init__(self, position, size, size)
		else:
			raise TypeError("position must be of type 'Coordinate'")

	@property
	def size(self):
		# It's a square. Width and height are the same
		return self.width


