from lib.shapes.Shape import Shape

class Element(object):
	"""Base class for a chart element."""

	def __init__(self, id=u'', classes=()):
		"""
		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings
		"""

		self.element = Shape()
		self.id = id
		if isinstance(classes, basestring):
			self.classes = (classes,)
		else:
			self.classes = tuple(classes)

	def getElement(self):
		"""Dummy method to retrieve the element's shapes."""

		pass
