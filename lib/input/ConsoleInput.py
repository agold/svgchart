import sys
import os
import fileinput

class ConsoleInput:
	"""Receives piped console input and passes it to the InputSets of rawInput."""

	def __init__(self,rawInput):
		"""Keyword arguments:
		rawInput -- The target RawInput.
		
		"""
		if (not os.isatty(sys.stdin.fileno())):
			text = u''
			for line in fileinput.input('-'):
				text += line
			rawInput.settings.input(text)
			rawInput.data.input(text)
			rawInput.scripts.input(text)