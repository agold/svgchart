from Coordinate import Coordinate

class Rectangle(object):
	"""Defines a rectangle of a given height and width beginning at some coordinate"""

	position = Coordinate()
	width = 0
	height = 0

	def __init__(self, position=Coordinate(), width=0, height=0):
		if isinstance(position, Coordinate):
			self.position = position
			self.width = width
			self.height = height
		else:
			raise TypeError("position must be of type 'Coordinate'")


