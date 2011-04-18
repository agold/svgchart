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
	>>> path = Path(coords)
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
	<path d="M 1.0,2.0 L 3.0,4.0 L 5.0,6.0" />

	"""
	
	def __init__(self, coordinates=()):
		"""Keyword arguments:
		coordinates -- an iterable of Coordinates

		"""

		for coord in coordinates:
			if not isinstance(coord, Coordinate):
				raise TypeError("Coordinates must be of type 'Coordinate'")

		Shape.__init__(self, tag=u'path')
		self.coordinates = tuple(coordinates)

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

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""
		
		self.attrs['d'] = self.pathString()

		return Shape.svg(self)
