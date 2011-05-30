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
	"""Parses an XML string into an IndexedDict tree.
	@param xml: The XML string
	@param dest: Target IndexedDict; if nonempty, it will be extended
	"""
	if (dest == None):
		dest = IndexedDict()
	elem = ETree.fromstring(xml)
	parseTree(dest,elem)
	return dest
	
def parseTree(dest,elem):
	"""Parses a tree of Elements into an IndexedDict tree.
	@param dest: Target IndexedDict; if nonempty, it will be extended
	@param elem: Root of the tree of Elements to be parsed
	"""
	attrib = dict(elem.items())
	for key in attrib:
		dest[key] = attrib[key]

	if (elem.text and elem.text.strip()):
		dest.text = elem.text.strip()
	else:
		dest.text = None

	append = ('append' in attrib and attrib['append'] == 'append')
	tagcount = dict()
	for child in list(elem):
		if (child.tag not in tagcount):
			tagcount[child.tag] = 0
			if (child.tag not in dest.keys()):
				dest[child.tag] = IndexedDict()
			if (len(dest[child.tag]) == 0 or append):
				tagcount[child.tag] = len(dest[child.tag])
				dest[child.tag].append(IndexedDict())
		else:
			tagcount[child.tag] += 1
			if (tagcount[child.tag] >= len(dest[child.tag])):
				dest[child.tag].append(IndexedDict())
		parseTree(dest[child.tag][tagcount[child.tag]],child)
