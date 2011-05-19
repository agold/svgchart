from Shape import Shape
from Coordinate import Coordinate

class Rectangle(Shape):
	"""Defines a rectangle.

	>>> from Coordinate import Coordinate
	>>> rect = Rectangle(position=Coordinate(1, 2), width=3.0, height=4.0, id=u'id', classes=u'class')
	>>> rect.position
	(1, 2)
	>>> rect.width
	3.0
	>>> rect.height
	4.0
	>>> print rect
	<rect class="class" height="4.0000" id="id" width="3.0000" x="1.0000" y="2.0000" />
	
	"""

	def __init__(self, position=Coordinate(), width=1.0, height=1.0, id=None, classes=None):
		"""Keyword arguments:
		@param position: A Coordinate defining the position in the SVG document
		@type position: Coordinate
		@param width: The width of the rectangle
		@param height: The height of the rectangle
		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings
		"""

		if isinstance(position, Coordinate):
			Shape.__init__(self, tag=u'rect', id=id, classes=classes)
			self.position = position
			self.width = float(width)
			self.height = float(height)
		else:
			raise TypeError("position must be of type 'Coordinate'")

	def fitToWidth(self, width=0.0):
		"""Fits shape to given width maintaining scale.

		@param width: The width to fit to
		"""
		if width <= 0:
			raise ValueError("width must be greater than 0")

		scalingFactor = 1.0 - ((self.width - float(width)) / self.width)
		self.width = width
		self.height = self.height * scalingFactor

	def fitToHeight(self, height=0.0):
		"""Fits shape to given height maintaining scale.

		@param height: The height to fit to
		"""

		if height <= 0:
			raise ValueError("height must be greater than 0")

		scalingFactor = 1.0 - ((self.height - float(height)) / self.height)
		self.width = self.width * scalingFactor
		self.height = height

	def translateTo(self, coord=Coordinate()):
		"""Translates the rectangle to the given coordinate.

		@param coord: The new coordinate to translate to
		@type coord: Coordinate
		"""

		oldx, oldy = self.position
		self.translate(x=coord.x - oldx, y=coord.y - oldy)

	def translate(self, x=0.0, y=0.0):
		"""Translates the rectangle by the given amounts.

		@param x: The amount to translate in the x-direction
		@param y: The amount to translate in the y-direction
		"""

		oldx, oldy = self.position
		self.position = Coordinate(oldx + x, oldy + y)

	def svg(self):
		"""Returns the SVG representation as an XML fragment."""
		
		self.attrs['x'] = self.position.x
		self.attrs['y'] = self.position.y
		self.attrs['width'] = self.width
		self.attrs['height'] = self.height

		return Shape.svg(self)