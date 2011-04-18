from Coordinate import Coordinate
from Shape import Shape
from Rectangle import Rectangle

class Square(Rectangle):
	"""Defines a square as a rectangle with equal height and width.

	Subclass of Square

	Examples:
	>>> from Coordinate import Coordinate
	>>> square = Square(position=Coordinate(1, 2), size=3)
	>>> square.position
	(1, 2)
	>>> square.size
	3
	>>> square.width
	3
	>>> square.height
	3
	>>> print square
	<rect height="3.0000" width="3.0000" x="1.0000" y="2.0000" />

	"""

	def __init__(self, position=Coordinate(), size=0):
		"""Keyword arguments:
		position -- a Coordinate defining the position in the SVG document
		size -- the size of the square, i.e. the length of each side

		"""

		if isinstance(position, Coordinate):
			Rectangle.__init__(self, position, size, size)
		else:
			raise TypeError("position must be of type 'Coordinate'")

	@property
	def size(self):
		"""Returns the size of the square."""
		
		# It's a square. Width and height are the same
		return self.width


