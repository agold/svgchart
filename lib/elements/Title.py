from lib.shapes.Text import Text
from lib.shapes.ShapeGroup import ShapeGroup
from lib.shapes.Coordinate import Coordinate
from Element import Element

class Title(Element):
	"""Element of a title and optional subtitle."""

	def __init__(self, title=u'', subtitle=u'',
				x=0.0, y=0.0, width=100.0, height=50.0,
				id=u'', classes=(),
				titleid=u'', titleclasses=(),
				subtitleid=u'', subtitleclasses=()):
		"""
		@param title: The text of the title
		@type title: string
		@param subtitle: The text of the subtitle
		@type subtitle: string or None
		@param x: The x coordinate to draw the title element at
		@param y: The y coordinate to draw the title element at
		@param width: The width of the title element (used for centering)
		@param height: The height of the title element (used for centering)

		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings

		@param titleid: The SVG document ID of the title text
		@type titleid: string
		@param titleclasses: Classnames to be applied to the title text
		@type titleclasses: string or sequence of strings

		@param subtitleid: The SVG document ID of the subtitle text
		@type subtitleid: string
		@param subtitleclasses: Classnames to be applied to the subtitle text
		@type subtitleclasses: string or sequence of strings
		"""

		Element.__init__(self)

		self.title = title
		self.subtitle = subtitle
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.id = id
		self.classes = classes
		self.titleid = titleid
		self.titleclasses = titleclasses
		self.subtitleid = subtitleid
		self.subtitleclasses = subtitleclasses


	def getElement(self):
		"""Returns the shapes of the y axis."""
		
		elements = []
		if not self.subtitle:
			titleelem = Text(text=self.title, id=self.titleid, classes=self.titleclasses)
			vcenter = self.y + (self.height - self.y) / 2
			hcenter = self.x + (self.width - self.x) / 2
			titleelem.position = Coordinate(hcenter, vcenter)
			elements.append(titleelem)
		else:
			titleelem = Text(text=self.title, id=self.titleid, classes=self.titleclasses)
			subtitleelem = Text(text=self.subtitle, id=self.subtitleid, classes=self.subtitleclasses)
			totalheight = titleelem.height + subtitleelem.height
			vcenter = self.y + (self.height - self.y) / 2
			hcenter = self.x + (self.width - self.x) / 2
			titleelem.position = Coordinate(hcenter, vcenter - totalheight / 2)
			subtitleelem.position = Coordinate(hcenter, vcenter + totalheight / 2)
			elements += [titleelem, subtitleelem]

		return ShapeGroup(elements, id=self.id, classes=self.classes)

