import xml.etree.ElementTree as ETree

class ParsedInput(object):
	"""Stores parsed input dictionaries for settings, data and scripts."""

	def __init__(self,rawInput):
		"""Sets up InputSets for settings, data and scripts."""
		self.settings = dict()
		self.data = dict()
		self.scripts = dict()
		for (src,dest) in ((rawInput.settings,self.settings),(rawInput.data,self.data),(rawInput.scripts,self.scripts)):
			for str in src.textlist:
				parseXml(dest,str)
		#parseXml(self.settings,rawInput.data.textlist[0])

def parseXml(dest,xml):
	elem = ETree.fromstring(xml)
	return parseTree(dest,elem)
	
def parseTree(dest,elem):
	dest.update(dict(elem.items()))
	text = 0
	if (elem.text):
		text = elem.text.strip()
	if (text):
		dest['text'] = text
	tags = ()
	for child in list(elem):
		if (child.tag in tags):
			# Make a list if already exists
			temp = dict()
			parseTree(temp,child)
			dest[child.tag] = dest[child.tag],temp
		else:
			# Otherwise, just set
			dest[child.tag] = dict()
			parseTree(dest[child.tag],child)
			tags = tags,child.tag