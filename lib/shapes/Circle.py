from Coordinate import Coordinate
from Shape import Shape
from Ellipse import Ellipse

class Circle(Ellipse):
	"""Defines a circle as an ellipse with equal radii.

	Subclass of Ellipse

	Public methods:
	svg() -- extends Shape.svg()

	Examples:
	>>> from Coordinate import Coordinate
	>>> circle = Circle(position=Coordinate(1, 2), radius=3)
	>>> circle.position
	(1, 2)
	>>> circle.radius
	3
	>>> circle.rx
	3
	>>> circle.ry
	3
	>>> print circle
	<circle cx="1.0000" cy="2.0000" r="3.0000" />

	"""

	def __init__(self, position=Coordinate(), radius=0):
		"""Keyword arguments:
		position -- a Coordinate defining the position in the SVG document
		radius -- the radius of the circle

		"""
		
		if isinstance(position, Coordinate):
			Ellipse.__init__(self, position, radius, radius)
			self.tag = u'circle'
		else:
			raise TypeError("position must be of type 'Coordinate'")

	@property
	def radius(self):
		"""Returns the radius of the circle."""
		return self.rx

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""

		self.attrs['cx'] = self.position.x
		self.attrs['cy'] = self.position.y
		self.attrs['r'] = self.radius

		return Shape.svg(self)
