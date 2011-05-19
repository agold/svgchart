from Coordinate import Coordinate
from Shape import Shape
from Path import Path

class Line(Path):
	"""A Path with 2 vertices.

	>>> from Coordinate import Coordinate
	>>> line = Line(start=Coordinate(1, 2), end=Coordinate(3, 4), id=u'id', classes=u'class')
	>>> line.start
	(1, 2)
	>>> line.end
	(3, 4)
	>>> print line
	<line class="class" id="id" x1="1.0000" x2="3.0000" y1="2.0000" y2="4.0000" />

	"""

	def __init__(self, start=Coordinate(), end=Coordinate(), id=None, classes=None):
		"""
		@param start: Coordinate of the first point of the line
		@type start: Coordinate
		@param end: Coordinate of the last point of the line
		@type end: Coordinate
		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings
		"""

		Path.__init__(self, (start, end), id=id, classes=classes)
		self.tag = u'line'

	@property
	def start(self):
		"""Returns the first point of the line."""

		return self.coordinates[0]

	@property
	def end(self):
		"""Returns the last point of the line."""

		return self.coordinates[1]

	def svg(self):
		"""Returns the SVG representation as an XML fragment."""

		self.attrs['x1'] = self.start.x
		self.attrs['y1'] = self.start.y
		self.attrs['x2'] = self.end.x
		self.attrs['y2'] = self.end.y

		return Shape.svg(self)