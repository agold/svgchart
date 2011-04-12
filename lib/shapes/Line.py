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

	@property
	def svg(self):
		svg = u'<line x1="{begin.x:.{fp:d}f}" y1="{begin.y:.{fp:d}f}" x2="{end.x:.{fp:d}f}" y2="{end.y:.{fp:d}f}" />'
		return svg.format(fp=self.precision, begin=self.begin, end=self.end)