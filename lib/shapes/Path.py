from Shape import Shape
from Coordinate import Coordinate

class Path(Shape):
	"""Defines a path from a tuple of Coordinates.

	Subclass of Shape

	Public methods:
	pathString() -- the SVG coordinate list as a string
	svg() -- extended from Shape.svg()

	Examples:
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
		"""Keyword arguments:
		coordinates -- an iterable of Coordinates
		id -- the unique ID to be used in the SVG document
		classes -- classnames to be used in the SVG document - string or iterable of classnames

		"""

		for coord in coordinates:
			if not isinstance(coord, Coordinate):
				raise TypeError("Coordinates must be of type 'Coordinate'")

		Shape.__init__(self, tag=u'path', id=id, classes=classes)
		self.coordinates = tuple(coordinates)

	@property
	def width(self):
		xcoords = [self.coordinates[i].x for i in xrange(len(self.coordinates))]
		return float(max(xcoords)) - float(min(xcoords))

	@property
	def height(self):
		ycoords = [self.coordinates[i].y for i in xrange(len(self.coordinates))]
		return float(max(ycoords)) - float(min(ycoords))

	@property
	def position(self):
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
		x, y = self.position
		ratio = width / self.width
		newcoords = []
		for coord in self.coordinates:
			newx = x + (coord.x - x) * ratio
			newy = y + (coord.y - y) * ratio
			newcoords.append(Coordinate(newx, newy))
		self.coordinates = tuple(newcoords)

	def fitToHeight(self, height=0.0):
		x, y = self.position
		ratio = height / self.height
		newcoords = []
		for coord in self.coordinates:
			newx = x + (coord.x - x) * ratio
			newy = y + (coord.y - y) * ratio
			newcoords.append(Coordinate(newx, newy))
		self.coordinates = tuple(newcoords)

	def translateTo(self, coord=Coordinate()):
		x = min([self.coordinates[i].x for i in xrange(len(self.coordinates))])
		y = min([self.coordinates[i].y for i in xrange(len(self.coordinates))])
		self.translate(x=coord.x - x, y=coord.y - y)

	def translate(self, x=0.0, y=0.0):
		newcoords = []
		for oldx, oldy in self.coordinates:
			newcoords.append(Coordinate(x + oldx, y + oldy))
		self.coordinates = tuple(newcoords)

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""
		
		self.attrs['d'] = self.pathString()

		return Shape.svg(self)