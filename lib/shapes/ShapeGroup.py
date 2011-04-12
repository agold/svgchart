from Shape import Shape

class ShapeGroup(Shape):
	"""Defines a grouping of shapes."""

	shapes = ()

	def __init__(self, shapes=()):
		for shape in shapes:
			if  not isinstance(shape, Shape):
				raise TypeError("shapes must contain only objects of type 'Shape'")

		self.shapes = tuple(shapes)

	def __iter__(self):
		for shape in self.shapes:
			yield shape

	@property
	def svg(self):
		svg = [u'<g>']
		for shape in self.shapes:
			try:
				svg += [shape.svg]
			except AttributeError:
				print u'AttributeError:', shape, u'has no svg attribute'

		svg += [u'</g>']
		return u'\n'.join(svg)
