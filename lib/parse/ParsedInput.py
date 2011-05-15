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

	if (elem.text):
		dest.text = elem.text.strip()
	else:
		dest.text = None
	
	for child in list(elem):
		append = ('append' in attrib and attrib['append'] == 'append')
		if (child.tag not in dest.keys()):
			dest[child.tag] = IndexedDict()
			dest[child.tag].append(IndexedDict())

		if (append):
			dest[child.tag].append(IndexedDict())
			parseTree(dest[child.tag][-1],child)
		else:
			parseTree(dest[child.tag][0],child)
