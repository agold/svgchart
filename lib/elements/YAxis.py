from Axis import Axis
from lib.shapes.Line import Line
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Text import Text
from lib.shapes.ShapeGroup import ShapeGroup

class YAxis(Axis):

	def __init__(self, min=0.0, max=1.0, start=0.0, end=1.0,
				 majorticks=5, minorticks=20,
				 majorlength=10, minorlength=5,
				 x=0.0,
				 id=u'', classes=(),
				 baseid=u'', baseclasses=(),
				 labelidprefix=u'', labelclasses=(),
				 majoridprefix=u'', majorclasses=(),
				 minoridprefix=u'', minorclasses=()):

		Axis.__init__(self, min=min, max=max, start=start, end=end,
				 majorticks=majorticks, minorticks=minorticks,
				 majorlength=majorlength, minorlength=minorlength,
				 id=id, classes=classes,
				 baseid=baseid, baseclasses=baseclasses,
				 labelidprefix=labelidprefix, labelclasses=labelclasses,
				 majoridprefix=majoridprefix, majorclasses=majorclasses,
				 minoridprefix=minoridprefix, minorclasses=minorclasses)

		self.x = float(x)
		self.width = float(majorlength if majorlength >= minorlength else minorlength)
		self.labelmargin = 10

	def getElement(self):
		ticks = self.ticks()
		lines = [Line(start=Coordinate(self.x + self.width, self.start),
						end=Coordinate(self.x + self.width, self.end),
						id=self.baseid, classes=self.baseclasses)]
		labels = []
		majorcount, minorcount = (0, 0)
		for tick in ticks:
			if tick['type'] is 'major':
				majorcount += 1
				lines.append(Line(start=Coordinate(self.x + self.width, tick['coord']),
							end=Coordinate(self.x  + self.width + self.majorlength, tick['coord']),
							id=u'{}-{:d}'.format(self.majoridprefix, majorcount),
							classes=self.majorclasses))
				labels.append(Text(position=Coordinate(self.x  + self.width - self.labelmargin, tick['coord']),
							text=str(tick['value']),
							id=u'{}-{:d}'.format(self.labelidprefix, majorcount),
							classes=self.labelclasses))
			else:
				minorcount += 1
				lines.append(Line(start=Coordinate(self.x + self.width , tick['coord']),
							end=Coordinate(self.x  + self.width + self.minorlength, tick['coord']),
							id=u'{}-{:d}'.format(self.minoridprefix, minorcount),
							classes=self.minorclasses))

		lines = ShapeGroup(lines, id=u'{}-lines'.format(self.id), classes=self.classes)
		labels = ShapeGroup(labels, id=u'{}-labels'.format(self.labelidprefix), classes=self.labelclasses)

		return ShapeGroup([lines, labels], id=self.id, classes=self.classes)

