from Grid import Grid
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Line import Line
from lib.shapes.ShapeGroup import ShapeGroup

class HorizontalGrid(Grid):

	def __init__(self, points=(), left=0.0, right=1.0,
				id=u'', classes=(),
				lineidprefix=u'', lineclasses=()):

		Grid.__init__(self, points, id, classes, lineidprefix, lineclasses)

		self.left = left
		self.right = right

	def getElement(self):
		
		lines = []
		linecount = 0
		for point in self.points:
			linecount += 1
			lines.append(Line(start=Coordinate(self.left, point),
						end=Coordinate(self.right, point),
						id=u'{}-{:d}'.format(self.lineidprefix, linecount),
						classes=self.lineclasses))

		return ShapeGroup(shapes=lines, id=self.id, classes=self.classes)

