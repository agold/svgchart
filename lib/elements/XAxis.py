from Axis import Axis
from lib.shapes.Line import Line
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Text import Text
from lib.shapes.ShapeGroup import ShapeGroup

class XAxis(Axis):

	def __init__(self, min=0.0, max=1.0, start=0.0, end=1.0,
				 majorticks=5, minorticks=20, y=0.0, height=20.0):

		Axis.__init__(self, min, max, start, end, majorticks, minorticks)

		self.y = float(y)
		self.height = float(height)
		self.labelmargin = 10

		ticks = self.ticks()
		lines = [Line(start=Coordinate(self.start, self.y + self.height),
						end=Coordinate(self.end, self.y + self.height))]
		labels = []
		for tick in ticks:
			if tick['type'] is 'major':
				lines.append(Line(start=Coordinate(tick['coord'], self.y + self.height),
							end=Coordinate(tick['coord'], self.y + self.height - self.majorlength)))
				labels.append(Text(position=Coordinate(tick['coord'], self.y + self.height + self.labelmargin), text=str(tick['value'])))
			else:
				lines.append(Line(start=Coordinate(tick['coord'], self.y + self.height),
							end=Coordinate(tick['coord'], self.y + self.height - self.minorlength)))

		lines = ShapeGroup(lines)
		labels = ShapeGroup(labels)
		self.element = ShapeGroup([lines, labels])



axis = XAxis(0, 1, 0, 500, 5, 20, 300, 20)
print axis.element