from Coordinate import Coordinate

class Ellipse(object):
	"""Defines an ellipse at a center coordinate with x-radius and y-radius"""

	center = Coordinate()
	rx = 0
	ry = 0
	
	def __init__(self, center=Coordinate(), rx=0, ry=0):
		if isinstance(center, Coordinate):
			self.center = center
			self.rx = rx
			self.ry = ry
		else:
			raise TypeError("center must be of type 'Coordinate'")

