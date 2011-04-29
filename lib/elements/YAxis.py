from Axis import Axis
from lib.shapes.Line import Line
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Text import Text
from lib.shapes.ShapeGroup import ShapeGroup

class YAxis(Axis):

	def __init__(self, min=0.0, max=1.0, start=0.0, end=1.0,
				 majorticks=5, minorticks=20, x=0.0):

		Axis.__init__(self, min, max, start, end, majorticks, minorticks)

		self.x = float(x)
		self.labelmargin = 10

		ticks = self.ticks()
		lines = [Line(start=Coordinate(self.x, self.start),
						end=Coordinate(self.x, self.end))]
		labels = []
		for tick in ticks:
			if tick['type'] is 'major':
				lines.append(Line(start=Coordinate(self.x, tick['coord']),
							end=Coordinate(self.x + self.majorlength, tick['coord'])))
				labels.append(Text(position=Coordinate(self.x - self.labelmargin, tick['coord']), text=str(tick['value'])))
			else:
				lines.append(Line(start=Coordinate(self.x, tick['coord']),
							end=Coordinate(self.x + self.minorlength, tick['coord'])))

		lines = ShapeGroup(lines)
		labels = ShapeGroup(labels)
		self.element = ShapeGroup([lines, labels])



axis = YAxis(0, 1, 0, 500, 5, 20, 50)
print axis.element

