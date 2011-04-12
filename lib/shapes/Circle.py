from Coordinate import Coordinate
from Ellipse import Ellipse

class Circle(Ellipse):
	"""Defines a circle as an ellipse with equal radii"""

	def __init__(self, position=Coordinate(), radius=0):
		if isinstance(position, Coordinate):
			Ellipse.__init__(self, position, radius, radius)
		else:
			raise TypeError("position must be of type 'Coordinate'")

	@property
	def radius(self):
		return self.rx

	@property
	def svg(self):
		svg = u'<circle cx="{pos.x:.{fp:d}f}" cy="{pos.y:.{fp:d}f}" r="{radius:.{fp:d}f}" />'
		return svg.format(fp=self.precision, pos=self.position, radius=self.radius)
