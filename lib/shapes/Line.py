from Coordinate import Coordinate
from Path import Path

class Line(Path):
	"""A Path of length 2."""
	
	def __init__(self, start=Coordinate(), end=Coordinate()):
		Path.__init__(self, (start, end))

	@property
	def begin(self):
		return self.coordinates[0]

	@property
	def end(self):
		return self.coordinates[1]