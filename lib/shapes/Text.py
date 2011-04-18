from Shape import Shape
from Coordinate import Coordinate

class Text(Shape):
	"""Defines a string of text beginning at some coordinate.

	Subclass of Shape

	Public methods:
	svg() -- extends Shape.svg()

	Examples:
	>>> from Coordinate import Coordinate
	>>> text = Text(position=Coordinate(1, 2), text='Hello world')
	>>> text.position
	(1, 2)
	>>> text.text
	'Hello world'
	>>> print text
	<text x="1.0000" y="2.0000">Hello world</text>

	"""
	
	def __init__(self, position=Coordinate(), text=u''):
		"""Keyword arguments:
		position -- a Coordinate defining the position in the SVG document
		text -- string of text

		"""

		if isinstance(position, Coordinate):
			Shape.__init__(self, tag=u'text')
			self.position = position
			self.text = text
		else:
			raise TypeError("position must be of type 'Coordinate'")

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()
		
		"""

		self.attrs['x'] = self.position.x
		self.attrs['y'] = self.position.y

		return Shape.svg(self)