from lib.shapes.Shape import Shape

class Element(object):
	def __init__(self, id=u'', classes=()):
		self.element = Shape()
		self.id = id
		if isinstance(classes, basestring):
			self.classes = (classes,)
		else:
			self.classes = tuple(classes)

	def getElement(self):
		pass
