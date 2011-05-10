from RawInput import RawInput
from FileInput import FileInput
from ConsoleInput import ConsoleInput

class InputLayer(object):
	"""Receives input XML documents.
	Makes them available through rawInput.
	"""

	def __init__(self,args):
		"""Keyword arguments:
		args -- Command-line option-value dictionary.
		"""
		ri = self.rawInput = RawInput()

		# Input from specified files
		#FileInput(self.rawInput,args['-input'],args['-settings'],args['-data'],args['-scripts'])

		# Input from general file
		if ('-input' in args):
			FileInput([ri.settings,ri.data,ri.scripts],args['-input'])

		# Input from specific files
		if ('-settings' in args):
			FileInput([ri.settings],args['-settings'])
		if ('-data' in args):
			FileInput([ri.data],args['-data'])
		if ('-scripts' in args):
			FileInput([ri.scripts],args['-scripts'])

		# Input from stdin
		ConsoleInput(self.rawInput)