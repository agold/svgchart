from InputSet import InputSet

class RawInput(object):
	"""Stores raw input sets for settings, data and scripts."""

	def __init__(self):
		"""Sets up InputSets for settings, data and scripts."""
		self.settings = InputSet('settings')
		self.data = InputSet('data')
		self.scripts = InputSet('scripts')