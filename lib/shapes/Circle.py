from Coordinate import Coordinate
from Shape import Shape
from Ellipse import Ellipse

class Circle(Ellipse):
	"""Defines a circle as an ellipse with equal radii.

	>>> from Coordinate import Coordinate
	>>> circle = Circle(center=Coordinate(1, 2), radius=3.0, id=u'id', classes=u'class')
	>>> circle.center
	(1, 2)
	>>> circle.radius
	3.0
	>>> circle.rx
	3.0
	>>> circle.ry
	3.0
	>>> print circle
	<circle class="class" cx="1.0000" cy="2.0000" id="id" r="3.0000" />

	"""

	def __init__(self, center=Coordinate(), radius=1.0, id=None, classes=None):
		"""
		@param center: A Coordinate defining the center in the SVG document
		@type center: Coordinate
		@param radius: The radius of the circle
		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings
		"""
		
		if isinstance(center, Coordinate):
			Ellipse.__init__(self, center, radius, radius, id, classes)
			self.tag = u'circle'
		else:
			raise TypeError("center must be of type 'Coordinate'")

	@property
	def radius(self):
		"""Returns the radius of the circle."""

		return self.rx

	def svg(self):
		"""Returns the SVG representation as an XML fragment."""

		self.attrs['cx'] = self.center.x
		self.attrs['cy'] = self.center.y
		self.attrs['r'] = self.radius

		return Shape.svg(self)
