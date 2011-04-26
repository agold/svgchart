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
	
	def __init__(self, position=Coordinate(), rx=1.0, ry=1.0):
		"""Keyword arguments:
		position -- a Coordinate defining the position in the SVG document
		rx -- the x-radius of the ellipse
		ry -- the y-radius of the ellipse

		"""
		
		if isinstance(position, Coordinate):
			Shape.__init__(self, tag=u'ellipse')
			self.position = position
			self.rx = float(rx)
			self.ry = float(ry)
		else:
			raise TypeError("position must be of type 'Coordinate'")

	def fitToWidth(self, width=0.0):
		"""Fits shape to given width maintaining scale."""
		if width <= 0:
			raise ValueError("width must be greater than 0")

		# Maintain scale. Divide by 2 since it's a radius
		scalingFactor = 1.0 - ((self.rx - float(width)) / self.rx)
		self.rx = width / 2.0
		self.ry = (self.ry * scalingFactor) / 2.0
		
	def fitToHeight(self, height=0.0):
		"""Fits shape to given height maintaining scale."""
		if height <= 0:
			raise ValueError("height must be greater than 0")

		# Maintain scale. Divide by 2 since it's a radius
		scalingFactor = 1.0 - ((self.ry - float(height)) / self.ry)
		self.rx = (self.rx * scalingFactor) / 2.0
		self.ry = height / 2.0
		
	def fit(self, width=0.0, height=0.0):
		"""Fits shape to given width and height maintaining scale."""
		if width <= 0 and height <= 0:
			raise ValueError("width or height must be greater than 0")

		if height < width and height > 0 or width <= 0:
			self.fitToHeight(height)
		else:
			self.fitToWidth(width)

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""

		self.attrs['cx'] = self.position.x
		self.attrs['cy'] = self.position.y
		self.attrs['rx'] = self.rx
		self.attrs['ry'] = self.ry

		return Shape.svg(self)