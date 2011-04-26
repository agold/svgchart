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
		#if (len(filename) > 0):
		#	f = open(filename)
		#	string = unicode(f.read())
		opentag = u'<' + self.tagName
		closetag = u'</' + self.tagName + u'>'
		start = string.find(opentag)
		end = string.find(closetag) + len(closetag)
		string = string[start:end]
		
		self.textlist.append(string)
