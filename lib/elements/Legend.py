from Element import Element
from lib.shapes.ShapeGroup import ShapeGroup
from lib.shapes.Circle import Circle
from lib.shapes.Square import Square
from lib.shapes.Text import Text
from lib.shapes.Coordinate import Coordinate

class Legend(Element):

	def __init__(self, entries=(), x=0.0, y=0.0,
				width=1.0, entryheight=12.0,
				title=u'Legend', titlesize=12.0,
				id=u'', classes=(),
				titleid=u'', titleclasses=(),
				entryidprefix=u'', entryclasses=(),
				entryshapeprefix=u'', entryshapeclasses=(),
				entrytextprefix=u'', entrytextclasses=()):

		Element.__init__(self, id=id, classes=classes)

		self.entries = entries
		self.x = x
		self.y = y
		self.width = width
		self.title = title
		self.titlesize = titlesize
		self.entryheight = entryheight
		self.titleid = titleid
		self.titleclasses = titleclasses
		self.entryidprefix = entryidprefix
		self.entryclasses = entryclasses
		self.entryshapeprefix = entryshapeprefix
		self.entryshapeclasses = entryshapeclasses
		self.entrytextprefix = entrytextprefix
		self.entrytextclasses = entrytextclasses

	def getElement(self):
		title = Text(text=self.title,
					position=Coordinate(self.x + self.width /2, self.y),
					fontsize=self.titlesize,
					id=self.titleid,
					classes=self.titleclasses)
		legend = [title]
		entrycount = 0
		for entry in self.entries:
			entrycount += 1
			shape = entry["shape"]
			text = entry["text"]

			shape.id = u"{}-{:d}".format(self.entryshapeprefix, entrycount)
			shape.classes = self.entryshapeclasses
			shape.fit(height=self.entryheight)
			shape.translateTo(Coordinate(self.x, self.y + self.titlesize + entrycount * self.entryheight))

			textelem = Text(position=Coordinate(self.x + shape.width, shape.position.y),
							text=text,
							fontsize=self.entryheight,
							id=u"{}-{:d}".format(self.entrytextprefix, entrycount),
							classes=self.entrytextclasses)
			legendentry = ShapeGroup([shape, textelem],
									id=u"{}-{:d}".format(self.entryidprefix, entrycount),
									classes=self.entryclasses)
			legend.append(legendentry)

		return ShapeGroup(legend, id=self.id, classes=self.classes)
