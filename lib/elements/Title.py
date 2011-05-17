from lib.shapes.Text import Text
from lib.shapes.ShapeGroup import ShapeGroup
from lib.shapes.Coordinate import Coordinate
from Element import Element

class Title(Element):

	def __init__(self, title=u'', subtitle=u'',
				x=0.0, y=0.0, width=100.0, height=50.0,
				id=u'', classes=(),
				titleid=u'', titleclasses=(),
				subtitleid=u'', subtitleclasses=()):

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

