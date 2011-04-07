from Coordinate import Coordinate
from Ellipse import Ellipse

class Circle(Ellipse):
	"""Defines a circle as an ellipse with equal radii"""

	def __init__(self, center=Coordinate(), radius=0):
		if isinstance(center, Coordinate):
			Ellipse.__init__(self, center, radius, radius)
		else:
			raise TypeError("center must be of type 'Coordinate'")

	@property
	def radius(self):
		return self.rx
