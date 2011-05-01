from parse.ParsedInput import ParsedInput

class ParsingLayer(object):

	def __init__(self,rawInput):
		self.parsedInput = ParsedInput(rawInput)