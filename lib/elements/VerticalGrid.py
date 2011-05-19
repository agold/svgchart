from Grid import Grid
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Line import Line
from lib.shapes.ShapeGroup import ShapeGroup

class VerticalGrid(Grid):

	def __init__(self, points=(), top=0.0, bottom=1.0,
				id=u'', classes=(),
				lineidprefix=u'', lineclasses=()):
		"""
		@param points: A sequence of points to draw grid lines at
		@param top: The top coordinate to begin drawing grid lines at
		@param bottom: The bottom coordinate to stop drawing grid lines at

		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings

		@param lineidprefix: The prefix for each grid line's ID
		@type lineidprefix: string
		@param lineclasses: Classnames to be applied to each grid line
		@type lineclasses: string or sequence of strings
		"""

		Grid.__init__(self, points, id, classes, lineidprefix, lineclasses)

		self.top = top
		self.bottom = bottom

	def getElement(self):
		"""Returns the shapes of the y axis."""
		
		lines = []
		linecount = 0
		for point in self.points:
			linecount += 1
			lines.append(Line(start=Coordinate(point, self.top),
						end=Coordinate(point, self.bottom),
						id=u'{}-{:d}'.format(self.lineidprefix, linecount),
						classes=self.lineclasses))

		return ShapeGroup(shapes=lines, id=self.id, classes=self.classes)



