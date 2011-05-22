from Element import Element
from lib.shapes.ShapeGroup import ShapeGroup
from lib.shapes.Text import Text
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Rectangle import Rectangle

class Legend(Element):
	"""A legend element."""
	
	def __init__(self, entries=(), x=0.0, y=0.0,
				width=1.0, height=1.0, entryheight=12.0,
				title=u'Legend', titlesize=12.0,
				id=u'', classes=(),
				titleid=u'', titleclasses=(),
				border=False, borderid=u'', borderclasses=()):
		"""
		@param entries: The legend entries. A sequence of dictionaries in the format {'shape': Shape, 'text': string}
		@param x: The x coordinate of the legend
		@param y: The y coordinate of the legend
		@param width: The width of the legend
		@param height: The height of the legend
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

		@param border: Flag designating whether or not to draw a border
		@type border: boolean
		@param borderid: The SVG document ID of the border element
		@type borderid: string
		@param borderclasses: Classnames to be applied to the border element
		@type borderclasses: string or sequence of strings
		"""

		Element.__init__(self, id=id, classes=classes)

		self.entries = entries
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.title = title
		self.titlesize = titlesize
		self.entryheight = entryheight
		self.titleid = titleid
		self.titleclasses = titleclasses
		self.border = border
		self.borderid = borderid
		self.borderclasses = borderclasses

	def getElement(self):
		"""Returns the shapes of the legend."""

		startx = self.x + 2.0
		starty = self.y + self.titlesize + 1.0
		legend = []
		if self.border:
			legend.append(Rectangle(Coordinate(self.x, self.y), width=self.width,
									height=self.height, id=self.borderid,
									classes=self.borderclasses))
		
		legend.append(Text(text=self.title,
						position=Coordinate(startx + self.width / 2, starty),
						fontsize=self.titlesize,
						id=self.titleid,
						classes=self.titleclasses))

		entrycount = 0
		for entry in self.entries:
			entrycount += 1

			shapename = entry["symbol"]["shape"].capitalize()
			text = entry["label"]
			shape = __import__('lib.shapes.' + shapename, globals(), locals(), [shapename])
			shape = getattr(shape, shapename)()

			shape.id = entry["legend-entry"]["symbol"]["id"]
			shape.classes = entry["legend-entry"]["symbol"]["class"]
			shape.fit(height=self.entryheight)
			shape.translateTo(Coordinate(startx, starty + self.titlesize + (entrycount - 1) * self.entryheight))

			textelem = Text(position=Coordinate(startx + shape.width, shape.position.y + self.entryheight - 1),
							text=text,
							fontsize=self.entryheight,
							id=entry["legend-entry"]["label"]["id"],
							classes=entry["legend-entry"]["label"]["class"])
			legendentry = ShapeGroup([shape, textelem],
									id=entry["legend-entry"]["id"],
									classes=entry["legend-entry"]["class"])
			legend.append(legendentry)

		return ShapeGroup(legend, id=self.id, classes=self.classes)
