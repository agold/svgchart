from Shape import Shape
from Coordinate import Coordinate

class Path(Shape):
	"""Defines a path from a tuple of Coordinates."""
	coordinates = ()
	
	def __init__(self, coordinates=()):
		if isinstance(coordinates, tuple):
			for coord in coordinates:
				if not isinstance(coord, Coordinate):
					raise TypeError("Coordinates must be of type 'Coordinate'")
			self.coordinates = coordinates
		else:
			raise TypeError("coordinates must be a tuple")

	@property
	def pathString(self):
		pathList = [u'M',
					u'{coord.x:.{fp:d}f},{coord.y:.{fp:d}f}'.format(
						fp=self.precision, coord=self.coordinates[0])]
		for coord in self.coordinates[1:]:
			pathList += [	u'L',
							u'{coord.x:.{fp:d}f},{coord.y:.{fp:d}f}'.format(
								fp=self.precision, coord=coord)]

		return u' '.join(pathList)

	@property
	def svg(self):
		svg = u'<path d="{path:s}" />'
		return svg.format(path=self.pathString)
