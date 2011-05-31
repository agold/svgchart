from ParsedInput import ParsedInput

class ParsingLayer(object):
	"""Parses XML input into an IndexedDict tree structure and makes it available through the parsedInput member."""

	def __init__(self,rawInput):
		"""
		@param rawInput: RawInput object containing XML input to be parsed
		"""
		self.parsedInput = ParsedInput(rawInput)