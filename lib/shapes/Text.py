from Coordinate import Coordinate

class Text(object):
	"""Defines a string of text beginning at some coordinate"""

	position = Coordinate()
	text = ""
	
	def __init__(self, position=Coordinate(), text=""):
		if isinstance(position, Coordinate):
			self.position = position
			self.text = text
		else:
			raise TypeError("position must be of type 'Coordinate'")

