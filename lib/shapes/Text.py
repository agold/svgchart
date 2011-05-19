from Shape import Shape
from Coordinate import Coordinate

class Text(Shape):
	"""Defines a string of text beginning at some coordinate.

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
		"""
		@param position: A Coordinate defining the position in the SVG document
		@type position: Coordinate
		@param text: The text of the element
		@type text: string
		@param fontsize: the fontsize of the text (for calculating width/height)
		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings
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
		"""The approximate width of the text element."""

		return self.fontsize / 2 * len(self.text)

	@property
	def height(self):
		"""The approximate height of the text element."""

		return self.fontsize

	def fitToWidth(self, width=0.0):
		"""Fits shape to given width maintaining scale.

		@param width: The width to fit to
		"""

		if width <= 0:
			raise ValueError("width must be greater than 0")

		scalingFactor = 1.0 - ((self.width - float(width)) / self.width)
		self.fontsize *= scalingFactor

	def fitToHeight(self, height=0.0):
		"""Fits shape to given height maintaining scale.

		@param height: The height to fit to
		"""

		if height <= 0:
			raise ValueError("height must be greater than 0")

		scalingFactor = 1.0 - ((self.height - float(height)) / self.height)
		self.fontsize *= scalingFactor

	def translateTo(self, coord=Coordinate()):
		"""Translates the text to the given coordinate.

		@param coord: The new coordinate to translate to
		@type coord: Coordinate
		"""

		oldx, oldy = self.position
		self.translate(x=coord.x - oldx, y=coord.y - oldy)

	def translate(self, x=0.0, y=0.0):
		"""Translates the text by the given amounts.

		@param x: The amount to translate in the x-direction
		@param y: The amount to translate in the y-direction
		"""

		oldx, oldy = self.position
		self.position = Coordinate(oldx + x, oldy + y)

	def svg(self):
		"""Returns the SVG representation as an XML fragment."""

		self.attrs['x'] = self.position.x
		self.attrs['y'] = self.position.y

		return Shape.svg(self)