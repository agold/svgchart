from Shape import Shape
from Coordinate import Coordinate

class Rectangle(Shape):
	"""Defines a rectangle.

	Subclass of Shape

	Public methods:
	svg() -- extended from Shape.svg()

	Examples:
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
		position -- a Coordinate defining the position in the SVG document
		width -- the width of the rectangle
		height -- the height of the rectangle
		id -- the unique ID to be used in the SVG document
		classes -- classnames to be used in the SVG document - string or iterable of classnames

		"""

		if isinstance(position, Coordinate):
			Shape.__init__(self, tag=u'rect', id=id, classes=classes)
			self.position = position
			self.width = float(width)
			self.height = float(height)
		else:
			raise TypeError("position must be of type 'Coordinate'")

	def fitToWidth(self, width=0.0):
		"""Fits shape to given width maintaining scale."""
		if width <= 0:
			raise ValueError("width must be greater than 0")

		scalingFactor = 1.0 - ((self.width - float(width)) / self.width)
		self.width = width
		self.height = self.height * scalingFactor

	def fitToHeight(self, height=0.0):
		"""Fits shape to given height maintaining scale."""
		if height <= 0:
			raise ValueError("height must be greater than 0")

		scalingFactor = 1.0 - ((self.height - float(height)) / self.height)
		self.width = self.width * scalingFactor
		self.height = height

	def translateTo(self, coord=Coordinate()):
		oldx, oldy = self.position
		self.translate(x=coord.x - oldx, y=coord.y - oldy)

	def translate(self, x=0.0, y=0.0):
		oldx, oldy = self.position
		self.position = Coordinate(oldx + x, oldy + y)

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""
		
		self.attrs['x'] = self.position.x
		self.attrs['y'] = self.position.y
		self.attrs['width'] = self.width
		self.attrs['height'] = self.height

		return Shape.svg(self)