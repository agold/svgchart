from Shape import Shape
from Coordinate import Coordinate

class Ellipse(Shape):
	"""Defines an ellipse at a center coordinate with x-radius and y-radius.

	Subclass of Shape

	Public methods:
	svg() -- extended from Shape.svg()

	Examples:
	>>> from Coordinate import Coordinate
	>>> ellipse = Ellipse(position=Coordinate(1, 2), rx=3, ry=4)
	>>> ellipse.position
	(1, 2)
	>>> ellipse.rx
	3
	>>> ellipse.ry
	4
	>>> print ellipse
	<ellipse cx="1.0000" cy="2.0000" rx="3.0000" ry="4.0000" />

	"""
	
	def __init__(self, position=Coordinate(), rx=0, ry=0):
		"""Keyword arguments:
		position -- a Coordinate defining the position in the SVG document
		rx -- the x-radius of the ellipse
		ry -- the y-radius of the ellipse

		"""
		
		if isinstance(position, Coordinate):
			Shape.__init__(self, tag=u'ellipse')
			self.position = position
			self.rx = rx
			self.ry = ry
		else:
			raise TypeError("position must be of type 'Coordinate'")

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""

		self.attrs['cx'] = self.position.x
		self.attrs['cy'] = self.position.y
		self.attrs['rx'] = self.rx
		self.attrs['ry'] = self.ry

		return Shape.svg(self)