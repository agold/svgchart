try:
	import xml.etree.cElementTree as ETree
except:
	import xml.etree.ElementTree as ETree
from IndexedDict import IndexedDict

class ParsedInput(object):
	"""Stores parsed input dictionaries for settings, data and scripts."""

	def __init__(self,rawInput):
		"""Sets up InputSets for settings, data and scripts."""
		self.settings = IndexedDict()
		self.data = IndexedDict()
		self.scripts = IndexedDict()
		for (src,dest) in ((rawInput.settings,self.settings),(rawInput.data,self.data),(rawInput.scripts,self.scripts)):
			for str in src.textlist:
				parseXml(dest,str)

def parseXml(dest,xml):
	elem = ETree.fromstring(xml)
	return parseTree(dest,elem)
	
def parseTree(dest,elem):
	attrib = dict(elem.items())
	for key in attrib:
		dest[key] = attrib[key]
	text = 0
	if (elem.text):
		text = elem.text.strip()
	if (text):
		dest.text = text
	
	for child in list(elem):
		childAttrib = dict(child.items())
		if ('id' in childAttrib):
			childId = childAttrib['id']
		else:
			childId = ""
		append = ('append' in attrib and attrib['append'] == 'append')
		if (child.tag not in dest.keys()):
			dest[child.tag] = IndexedDict()
			if (childId):
				dest[child.tag][childId] = IndexedDict()
			else:
				dest[child.tag].append(IndexedDict())
		elif (childId and childId not in dest[child.tag].keys()):
			dest[child.tag][childId] = IndexedDict()
		elif (append):
			dest[child.tag].append(IndexedDict())

		if (childId):
			parseTree(dest[child.tag][childId],child)
		elif (append):
			parseTree(dest[child.tag][-1],child)
		else:
			parseTree(dest[child.tag][0],child)
