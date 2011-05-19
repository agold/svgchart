from Shape import Shape
from Coordinate import Coordinate

class Ellipse(Shape):
	"""Defines an ellipse at a center coordinate with x-radius and y-radius.

	>>> from Coordinate import Coordinate
	>>> ellipse = Ellipse(center=Coordinate(1, 2), rx=3.0, ry=4.0, id=u'id', classes=u'class')
	>>> ellipse.center
	(1, 2)
	>>> ellipse.rx
	3.0
	>>> ellipse.ry
	4.0
	>>> ellipse.position
	(-2.0, -2.0)
	>>> print ellipse
	<ellipse class="class" cx="1.0000" cy="2.0000" id="id" rx="3.0000" ry="4.0000" />

	"""
	
	def __init__(self, center=Coordinate(), rx=1.0, ry=1.0, id=None, classes=None):
		"""
		@param center: -- a Coordinate defining the center coordinate in the SVG document
		@type center: Coordinate
		@param rx: -- the x-radius of the ellipse
		@param ry: -- the y-radius of the ellipse
		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings
		"""
		
		if isinstance(center, Coordinate):
			Shape.__init__(self, tag=u'ellipse', id=id, classes=classes)
			self.center = center
			self.rx = float(rx)
			self.ry = float(ry)
		else:
			raise TypeError("center must be of type 'Coordinate'")

	@property
	def position(self):
		"""The top-left coordinate of the top-left corner of the ellipse's bounding rectangle."""

		return Coordinate(self.center.x - self.rx, self.center.y - self.ry)

	@property
	def width(self):
		"""The width of the ellipse."""

		return self.rx * 2.0

	@property
	def height(self):
		"""The height of the ellipse."""
		return self.ry * 2.0

	def fitToWidth(self, width=0.0):
		"""Fits shape to given width maintaining scale.

		@param width: The width to fit to
		"""

		if width <= 0:
			raise ValueError("width must be greater than 0")

		# Maintain scale. Divide by 2 since it's a radius
		scalingFactor = 1.0 - ((self.rx - float(width)) / self.rx)
		self.rx = width / 2.0
		self.ry = (self.ry * scalingFactor) / 2.0
		
	def fitToHeight(self, height=0.0):
		"""Fits shape to given height maintaining scale.

		@param height: The height to fit to
		"""

		if height <= 0:
			raise ValueError("height must be greater than 0")

		# Maintain scale. Divide by 2 since it's a radius
		scalingFactor = 1.0 - ((self.ry - float(height)) / self.ry)
		self.rx = (self.rx * scalingFactor) / 2.0
		self.ry = height / 2.0

	def translateTo(self, coord=Coordinate()):
		"""Translates the ellipse to the given coordinate.

		@param coord: The new coordinate to translate to
		@type coord: Coordinate
		"""

		oldx, oldy = self.center
		self.translate(x=coord.x - oldx + self.rx, y=coord.y - oldy + self.ry)

	def translate(self, x=0.0, y=0.0):
		"""Translates the ellipse by the given amounts.

		@param x: The amount to translate in the x-direction
		@param y: The amount to translate in the y-direction
		"""

		oldx, oldy = self.center
		self.center = Coordinate(oldx + x, oldy + y)

	def svg(self):
		"""Returns the SVG representation as an XML fragment."""

		self.attrs['cx'] = self.center.x
		self.attrs['cy'] = self.center.y
		self.attrs['rx'] = self.rx
		self.attrs['ry'] = self.ry

		return Shape.svg(self)
