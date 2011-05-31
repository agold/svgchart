class FileInput:
	"""Retrieves the contents of a file and passes them to InputSets."""

	def __init__(self,inputSets,filename):
		"""
		@param inputSets: List of target InputSets
		@param filename: Name of file to be scanned for input
		"""
		with open(filename,'rU') as f:
			text = f.read()
			for i in inputSets:
				i.input(text)