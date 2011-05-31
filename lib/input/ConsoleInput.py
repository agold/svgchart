import sys
import os
import fileinput

class ConsoleInput:
	"""Receives piped console input and passes it to the InputSets of rawInput."""

	def __init__(self,inputSets):
		"""
		@param inputSets: List of target InputSets
		"""
		if (not os.isatty(sys.stdin.fileno())):
			text = u''
			for line in fileinput.input('-'):
				text += line
			for i in inputSets:
				i.input(text)