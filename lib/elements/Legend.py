from Element import Element
from lib.shapes.ShapeGroup import ShapeGroup
from lib.shapes.Text import Text
from lib.shapes.Coordinate import Coordinate

class Legend(Element):
	"""A legend element."""
	
	def __init__(self, entries=(), x=0.0, y=0.0,
				width=1.0, entryheight=12.0,
				title=u'Legend', titlesize=12.0,
				id=u'', classes=(),
				titleid=u'', titleclasses=(),
				entryidprefix=u'', entryclasses=(),
				entryshapeprefix=u'', entryshapeclasses=(),
				entrytextprefix=u'', entrytextclasses=()):
		"""
		@param entries: The legend entries. A sequence of dictionaries in the format {'shape': Shape, 'text': string}
		@param x: The x coordinate of the legend
		@param y: The y coordinate of the legend
		@param width: The width of the legend
		@param entryheight: The height of each legend entry
		@param title: The title of the legend
		@type title: string or None
		@param titlesize: The size of the title text

		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings

		@param titleid: The SVG document ID of the title element
		@type titleid: string
		@param titleclasses: Classnames to be applied to the title element
		@type titleclasses: string or sequence of strings

		@param entryidprefix: The prefix for each legend entry's ID
		@type entryidprefix: string
		@param entryclasses: Classnames to be applied to each entry elements
		@type entryclasses: string or sequence of strings

		@param entryshapeprefix: The prefix for each legend entry shape's ID
		@type entryshapeprefix: string
		@param entryshapeclasses: Classnames to be applied to each entry shape
		@type entryshapeclasses: string or sequence of strings

		@param entrytextprefix: The prefix for each legend entry label ID
		@type entrytextprefix: string
		@param entrytextclasses: Classnames to be applied to each entry label
		@type entrytextclasses: string or sequence of strings
		"""

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
		"""Returns the shapes of the legend."""
		
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
