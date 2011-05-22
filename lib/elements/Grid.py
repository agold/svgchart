from Element import Element

class Grid(Element):
	"""Base class for a grid element."""

	def __init__(self, points=(),
				 start=0.0, end=1.0,
				 id=u'', classes=(),
				 lineidprefix=u'', lineclasses=()):
		"""
		@param points: A sequence of points to draw grid lines at

		@param start: The starting coordinate of the axis
		@param end: The ending coordinate of the axis

		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings

		@param lineidprefix: The prefix for each grid line's ID
		@type lineidprefix: string
		@param lineclasses: Classnames to be applied to each grid line
		@type lineclasses: string or sequence of strings
		"""

		self.points = tuple(points)
		self.start = start
		self.end = end
		self.id = id
		self.classes = classes
		self.lineidprefix = lineidprefix
		self.lineclasses = lineclasses
