from Shape import Shape
from Coordinate import Coordinate

class Path(Shape):
	"""Defines a path from a tuple of Coordinates.

	>>> from Coordinate import Coordinate
	>>> coords = (Coordinate(1, 2), Coordinate(3, 4), Coordinate(5, 6))
	>>> path = Path(coords, u'the-id', u'the class')
	>>> path.precision = 1
	>>> for coord in path.coordinates:
	...		print coord
	...
	(1, 2)
	(3, 4)
	(5, 6)
	>>> print path.pathString()
	M 1.0,2.0 L 3.0,4.0 L 5.0,6.0
	>>> print path
	<path class="the class" d="M 1.0,2.0 L 3.0,4.0 L 5.0,6.0" id="the-id" />

	"""
	
	def __init__(self, coordinates=(), id=None, classes=None):
		"""
		@param coordinates: The coordinates of the path's vertices
		@type coordinates: Sequence of Coordinates
		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings

		"""

		for coord in coordinates:
			if not isinstance(coord, Coordinate):
				raise TypeError("Coordinates must be of type 'Coordinate'")

		Shape.__init__(self, tag=u'path', id=id, classes=classes)
		self.coordinates = tuple(coordinates)

	@property
	def width(self):
		"""The width of the path."""

		xcoords = [self.coordinates[i].x for i in xrange(len(self.coordinates))]
		return float(max(xcoords)) - float(min(xcoords))

	@property
	def height(self):
		"""The height of the path."""

		ycoords = [self.coordinates[i].y for i in xrange(len(self.coordinates))]
		return float(max(ycoords)) - float(min(ycoords))

	@property
	def position(self):
		"""The top-left coodinate of the path."""

		x = min([self.coordinates[i].x for i in xrange(len(self.coordinates))])
		y = min([self.coordinates[i].y for i in xrange(len(self.coordinates))])
		return Coordinate(x, y)
	
	def pathString(self):
		"""Returns the SVG coordinate list as a string."""

		pathList = [u'M',
					u'{coord.x:.{fp:d}f},{coord.y:.{fp:d}f}'.format(
						fp=self.precision, coord=self.coordinates[0])]
		for coord in self.coordinates[1:]:
			pathList += [	u'L',
							u'{coord.x:.{fp:d}f},{coord.y:.{fp:d}f}'.format(
								fp=self.precision, coord=coord)]

		return u' '.join(pathList)

	def fitToWidth(self, width=0.0):
		"""Scales the path to fit in the given width.

		@param width: The width to scale to
		"""

		x, y = self.position
		ratio = width / self.width
		newcoords = []
		for coord in self.coordinates:
			newx = x + (coord.x - x) * ratio
			newy = y + (coord.y - y) * ratio
			newcoords.append(Coordinate(newx, newy))
		self.coordinates = tuple(newcoords)

	def fitToHeight(self, height=0.0):
		"""Scales the path to fit in the given height.

		@param height: The height to scale to
		"""

		x, y = self.position
		ratio = height / self.height
		newcoords = []
		for coord in self.coordinates:
			newx = x + (coord.x - x) * ratio
			newy = y + (coord.y - y) * ratio
			newcoords.append(Coordinate(newx, newy))
		self.coordinates = tuple(newcoords)

	def translateTo(self, coord=Coordinate()):
		"""Translates the path to the given coordinate.

		@param coord: The new coordinate to translate to
		@type coord: Coordinate
		"""

		x = min([self.coordinates[i].x for i in xrange(len(self.coordinates))])
		y = min([self.coordinates[i].y for i in xrange(len(self.coordinates))])
		self.translate(x=coord.x - x, y=coord.y - y)

	def translate(self, x=0.0, y=0.0):
		"""Translates the path by the given amounts.

		@param x: The amount to translate in the x-direction
		@param y: The amount to translate in the y-direction
		"""

		newcoords = []
		for oldx, oldy in self.coordinates:
			newcoords.append(Coordinate(x + oldx, y + oldy))
		self.coordinates = tuple(newcoords)

	def svg(self):
		"""Returns the SVG representation as an XML fragment."""
		
		self.attrs['d'] = self.pathString()

		return Shape.svg(self)