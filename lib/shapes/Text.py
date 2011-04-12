from Shape import Shape
from Coordinate import Coordinate

class Text(Shape):
	"""Defines a string of text beginning at some coordinate"""

	position = Coordinate()
	text = u''
	tagName = u'text'
	
	def __init__(self, position=Coordinate(), text=u''):
		if isinstance(position, Coordinate):
			self.position = position
			self.text = text
		else:
			raise TypeError("position must be of type 'Coordinate'")

	@property
	def svg(self):
		svg = u'<text x="{pos.x:.{fp:d}f}" y="{pos.y:.{fp:d}f}">{text:s}</text>'
		return svg.format(fp=self.precision, pos=self.position, text=self.text)

