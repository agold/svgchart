from Shape import Shape
from Coordinate import Coordinate

class Rectangle(Shape):
	"""Defines a rectangle.

	Subclass of Shape

	Public methods:
	svg() -- extended from Shape.svg()

	Examples:
	>>> from Coordinate import Coordinate
	>>> rect = Rectangle(position=Coordinate(1, 2), width=3, height=4)
	>>> rect.position
	(1, 2)
	>>> rect.width
	3
	>>> rect.height
	4
	>>> print rect
	<rect height="4.0000" width="3.0000" x="1.0000" y="2.0000" />
	
	"""

	def __init__(self, position=Coordinate(), width=0, height=0):
		"""Keyword arguments:
		position -- a Coordinate defining the position in the SVG document
		width -- the width of the rectangle
		height -- the height of the rectangle

		"""

		if isinstance(position, Coordinate):
			Shape.__init__(self, tag=u'rect')
			self.position = position
			self.width = width
			self.height = height
		else:
			raise TypeError("position must be of type 'Coordinate'")

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""
		
		self.attrs['x'] = self.position.x
		self.attrs['y'] = self.position.y
		self.attrs['width'] = self.width
		self.attrs['height'] = self.height

		return Shape.svg(self)