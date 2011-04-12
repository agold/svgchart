from Shape import Shape
from Coordinate import Coordinate

class Ellipse(Shape):
	"""Defines an ellipse at a center coordinate with x-radius and y-radius"""

	position = Coordinate()
	rx = 0
	ry = 0
	
	def __init__(self, position=Coordinate(), rx=0, ry=0):
		if isinstance(position, Coordinate):
			self.position = position
			self.rx = rx
			self.ry = ry
		else:
			raise TypeError("position must be of type 'Coordinate'")

	@property
	def svg(self):
		svg = u'<ellipse cx="{pos.x:.{fp:d}f}" cy="{pos.y:.{fp:d}f}" rx="{rx:.{fp:d}f}" ry="{ry:.{fp:d}f}" />'
		return svg.format(	fp=self.precision, pos=self.position,
							rx=self.rx, ry=self.ry)