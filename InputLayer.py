from input.RawInput import RawInput
from input.FileInput import FileInput
from input.ConsoleInput import ConsoleInput

class InputLayer(object):
	"""Receives input XML documents.
	Makes them available through rawInput.
	"""

	def __init__(self,args):
		"""Keyword arguments:
		args -- Command-line option-value dictionary.
		"""
		self.rawInput = RawInput()

		# Input from specified files
		FileInput(self.rawInput,args['-input'],args['-settings'],args['-data'],args['-scripts'])

		# Input from stdin
		ConsoleInput(self.rawInput)