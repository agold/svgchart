import re;

class InputSet(object):
	"""Base class for types of data input."""
	
	def __init__(self,tagName):
		"""Keyword arguments:
		tagName -- Name of the tag that delimits the pertinent input set(s).

		"""
		self.tagName = tagName
		self.textlist = []

	# Process string and extract first pertinent section
	def input(self,string = u''):
		"""Processes string and extracts the first pertinent section as
		a new entry in textlist.

		Keyword arguments:
		string -- string containing material to be searched for
					pertinent information

		"""
		match = re.search(r'<'+self.tagName+r'( [^>]+)? *((\/>)|(>.*<\/'+self.tagName+r'>))',string,re.DOTALL)
		if (match):
			self.textlist.append(match.group())