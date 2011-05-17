from Element import Element

class Grid(Element):

	def __init__(self, points=(),
				 id=u'', classes=(),
				 lineidprefix=u'', lineclasses=()):

		self.points = tuple(points)
		self.id = id
		self.classes = classes
		self.lineidprefix = lineidprefix
		self.lineclasses = lineclasses
