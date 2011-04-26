class FileInput:
	"""Retrieves the contents of a file as a string."""

	def __init__(self,rawInput,input = '',settings = '',data = '',scripts = ''):
		"""Keyword arguments:
		rawInput -- The target RawInput.
		input -- Filename containing input for any/all of the categories.
		settings -- Filename containing settings input.
		data -- Filename containing data input.
		scripts -- Filename containing scripts input.

		"""
		if (input):
			f = open(input,'rU')
			text = f.read()
			f.close()
			rawInput.settings.input(text)
			rawInput.data.input(text)
			rawInput.scripts.input(text)
		if (settings):
			f = open(settings,'rU')
			text = f.read()
			f.close()
			rawInput.settings.input(text)
		if (data):
			f = open(data,'rU')
			text = f.read()
			f.close()
			rawInput.data.input(text)
		if (scripts):
			f = open(scripts,'rU')
			text = f.read()
			f.close()
			rawInput.scripts.input(text)