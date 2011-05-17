from Shape import Shape
from Coordinate import Coordinate

class Text(Shape):
	"""Defines a string of text beginning at some coordinate.

	Subclass of Shape

	Public methods:
	svg() -- extends Shape.svg()

	Examples:
	>>> from Coordinate import Coordinate
	>>> text = Text(position=Coordinate(1, 2), text='Hello world', fontsize=12.0, id=u'id', classes=u'class')
	>>> text.position
	(1, 2)
	>>> text.text
	'Hello world'
	>>> text.fontsize
	12.0
	>>> print text
	<text class="class" id="id" x="1.0000" y="2.0000">Hello world</text>

	"""
	
	def __init__(self, position=Coordinate(), text=u'', fontsize=12.0,
				id=None, classes=None):
		"""Keyword arguments:
		position -- a Coordinate defining the position in the SVG document
		text -- string of text
		fontsize -- the fontsize of the text (for calculating width/height)
		id -- the unique ID to be used in the SVG document
		classes -- classnames to be used in the SVG document - string or iterable of classnames

		"""

		if isinstance(position, Coordinate):
			Shape.__init__(self, tag=u'text', id=id, classes=classes)
			self.position = position
			self.text = text
			self.fontsize = fontsize
		else:
			raise TypeError("position must be of type 'Coordinate'")

	@property
	def width(self):
		return self.fontsize / 2 * len(self.text)

	@property
	def height(self):
		return self.fontsize

	def fitToWidth(self, width=0.0):
		"""Fits shape to given width maintaining scale."""
		if width <= 0:
			raise ValueError("width must be greater than 0")

		scalingFactor = 1.0 - ((self.width - float(width)) / self.width)
		self.fontsize *= scalingFactor

	def fitToHeight(self, height=0.0):
		"""Fits shape to given height maintaining scale."""
		if height <= 0:
			raise ValueError("height must be greater than 0")

		scalingFactor = 1.0 - ((self.height - float(height)) / self.height)
		self.fontsize *= scalingFactor

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

		return Shape.svg(self)