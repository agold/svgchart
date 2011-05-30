from RawInput import RawInput
from FileInput import FileInput
from ConsoleInput import ConsoleInput

class InputLayer(object):
	"""Receives input XML documents.
	Makes them available through rawInput.
	"""

	def __init__(self, input=None, settings=None, data=None, scripts=None, type='scatter'):
		"""
		@param input: Filename for a unified input document
		@param settings: Filename for the settings
		@param data: Filename for the data
		@param scripts: Filename for the scripts
		@param type: Chart type name to specify default settings

		"""

		ri = self.rawInput = RawInput()

		# Default settings input
		FileInput([ri.settings],'defaults/default.' + type + '.settings.xml')

		# Input from general file
		if input is not None:
			FileInput([ri.settings,ri.data,ri.scripts], input)

		# Input from specific files
		if settings is not None:
			FileInput([ri.settings], settings)
		if data is not None:
			FileInput([ri.data], data)
		if scripts is not None:
			FileInput([ri.scripts], scripts)

		# Input from stdin
		ConsoleInput(self.rawInput)