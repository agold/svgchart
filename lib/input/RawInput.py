from InputSet import InputSet

class RawInput(object):
	"""Stores raw input sets for settings, data and scripts."""

	def __init__(self):
		self.settings = InputSet('settings')
		self.data = InputSet('data')
		self.scripts = InputSet('scripts')