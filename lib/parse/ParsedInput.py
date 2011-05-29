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
				parseXml(str,dest)

def parseXml(xml,dest = None):
	if (dest == None):
		dest = IndexedDict()
	elem = ETree.fromstring(xml)
	parseTree(dest,elem)
	return dest
	
def parseTree(dest,elem):
	attrib = dict(elem.items())
	for key in attrib:
		dest[key] = attrib[key]

	if (elem.text and elem.text.strip()):
		dest.text = elem.text.strip()
	else:
		dest.text = None

	append = ('append' in attrib and attrib['append'] == 'append')
	taglist = []
	for child in list(elem):
		if (child.tag not in taglist):
			taglist.append(child.tag)
			if (child.tag not in dest.keys() or not append):
				dest[child.tag] = IndexedDict()
		"""if (child.tag not in taglist and not append):
			dest[child.tag] = IndexedDict()
			taglist.append(child.tag)"""
		dest[child.tag].append(IndexedDict())
		parseTree(dest[child.tag][-1],child)
