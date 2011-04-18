from Shape import Shape
import xml.etree.ElementTree as etree

class ShapeGroup(Shape):
	"""Defines a grouping of shapes.

	Subclass of Shape

	Public methods:
	svg() -- returns the SVG representation as an XML fragment

	Examples:
	>>> from Shape import Shape
	>>> shapes = (Shape('foo'), Shape('bar'), Shape('baz'))
	>>> group = ShapeGroup(shapes)
	>>> for shape in group:
	...		print shape
	...
	<foo />
	<bar />
	<baz />
	>>> print group
	<g><foo /><bar /><baz /></g>

	"""

	def __init__(self, shapes=()):
		"""Keyword arguments:
		shapes -- iterable of Shapes to be included in the group

		"""
		for shape in shapes:
			if  not isinstance(shape, Shape):
				raise TypeError("shapes must contain only objects of type 'Shape'")

		self.shapes = tuple(shapes)

	def __iter__(self):
		for shape in self.shapes:
			yield shape

	def svg(self):
		"""Returns the SVG representation as an XML fragment.

		Extends Shape.svg()

		"""

		svg = etree.Element(tag=u'g')
		for shape in self.shapes:
			try:
				svg.append(shape.svg())
			except AttributeError:
				raise

		return svg
