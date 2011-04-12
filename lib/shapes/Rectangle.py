from Shape import Shape
from Coordinate import Coordinate

class Rectangle(Shape):
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

	@property
	def svg(self):
		svg = u'<rect x="{pos.x:.{fp:d}f}" y="{pos.y:.{fp:d}f}" width="{width:.{fp:d}f}" height="{height:.{fp:d}f}" />'
		return svg.format(	fp=self.precision, pos=self.position,
							width=self.width, height=self.height)