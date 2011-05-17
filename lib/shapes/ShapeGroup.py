from Coordinate import Coordinate
from Shape import Shape

class ShapeGroup(Shape):
	"""Defines a grouping of shapes.

	Subclass of Shape

	Public methods:
	svg() -- returns the SVG representation as an XML fragment

	Examples:
	>>> from Shape import Shape
	>>> shapes = (Shape('foo'), Shape('bar'), Shape('baz'))
	>>> group = ShapeGroup(shapes, id=u'id', classes=u'class')
	>>> for shape in group:
	...		print shape
	...
	<foo />
	<bar />
	<baz />
	>>> print group
	<g class="class" id="id"><foo /><bar /><baz /></g>

	"""

	def __init__(self, shapes=(), id=None, classes=None):
		"""Keyword arguments:
		shapes -- iterable of Shapes to be included in the group
		id -- the unique ID to be used in the SVG document
		classes -- classnames to be used in the SVG document - string or iterable of classnames

		"""

		for shape in shapes:
			if  not isinstance(shape, Shape):
				raise TypeError("shapes must contain only objects of type 'Shape'")

		Shape.__init__(self, tag=u'g', id=id, classes=classes)
		self.shapes = tuple(shapes)

	def __iter__(self):
		for shape in self.shapes:
			yield shape

	@property
	def width(self):
		maxcoord = None
		maxwidth = None
		mincoord = self.shapes[0].position.x
		for shape in self.shapes:
			if float(shape.position.x) < mincoord:
				mincoord = float(shape.position.x)

			if float(shape.position.x) >= maxcoord:
				maxcoord = float(shape.position.x)
				if float(shape.width) > maxwidth:
					maxwidth = float(shape.width)

		return maxcoord + maxwidth - mincoord

	@property
	def height(self):
		maxcoord = None
		maxwidth = None
		mincoord = self.shapes[0].position.y
		for shape in self.shapes:
			if float(shape.position.y) < mincoord:
				mincoord = float(shape.position.y)

			if float(shape.position.y) >= maxcoord:
				maxcoord = float(shape.position.y)
				if float(shape.height) > maxwidth:
					maxwidth = float(shape.height)

		return maxcoord + maxwidth - mincoord

	@property
	def position(self):
		x = min([self.shapes[i].position.x for i in xrange(len(self.shapes))])
		y = min([self.shapes[i].position.y for i in xrange(len(self.shapes))])
		return Coordinate(x, y)

	def fitToWidth(self, width=0.0):
		# NOTE: both width and height fitting methods are currently wrong
		# They should scale each shape and translate proportionally towards upper left
		scalingfactor = 1.0 - ((self.width - float(width)) / self.width)
		for shape in self.shapes:
			distx = shape.position.x - self.position.x
			disty = shape.position.y - self.position.y
			shape.fitToWidth(shape.width * scalingfactor)
			shape.translate(-distx * scalingfactor**2, -disty * scalingfactor**2)
	
	def fitToHeight(self, height=0.0):
		# NOTE: both width and height fitting methods are currently wrong
		# They should scale each shape and translate proportionally towards upper left
		scalingfactor = 1.0 - ((self.height - float(height)) / self.height)
		for shape in self.shapes:
			distx = shape.position.x - self.position.x
			disty = shape.position.y - self.position.y
			shape.fitToHeight(shape.height * scalingfactor)
			shape.translate(-distx * scalingfactor**2, -disty * scalingfactor**2)

	def translateTo(self, coord=Coordinate()):
		oldx, oldy = self.position
		self.translate(coord.x - oldx, coord.y - oldy)

	def translate(self, x=0.0, y=0.0):
		for shape in self.shapes:
			shape.translate(x, y)

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""

		shapes = []
		for shape in self.shapes:
			try:
				shapes.append(shape.svg())
			except AttributeError:
				raise

		self.subelements = shapes

		return Shape.svg(self)
