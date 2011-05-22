from Grid import Grid
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Line import Line
from lib.shapes.ShapeGroup import ShapeGroup

class HorizontalGrid(Grid):

	def __init__(self, points=(), left=0.0, right=1.0,
				start=0.0, end=1.0,
				id=u'', classes=(),
				lineidprefix=u'', lineclasses=()):
		"""
		@param points: A sequence of points to draw grid lines at
		@param left: The leftmost coordinate to begin drawing grid lines at
		@param right: The rightmost coordinate to stop drawing grid lines at

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

		Grid.__init__(self, points, start, end, id, classes, lineidprefix, lineclasses)

		self.left = left
		self.right = right

	def getElement(self):
		"""Returns the shapes of the y axis."""
		
		lines = []
		linecount = 0
		for point in self.points:
			if point != self.start and point != self.end:
				linecount += 1
				lines.append(Line(start=Coordinate(self.left, point),
							end=Coordinate(self.right, point),
							id=u'{}-{:d}'.format(self.lineidprefix, linecount),
							classes=self.lineclasses))

		return ShapeGroup(shapes=lines, id=self.id, classes=self.classes)

