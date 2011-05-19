from Element import Element

class Axis(Element):
	"""The base class for an axis element."""

	def __init__(self, min=0.0, max=1.0, start=0.0, end=1.0,
				 majorticks=5, minorticks=20,
				 majorlength=10, minorlength=5,
				 id=u'', classes=(),
				 baseid=u'', baseclasses=(),
				 labelidprefix=u'', labelclasses=(),
				 majoridprefix=u'', majorclasses=(),
				 minoridprefix=u'', minorclasses=()):
		"""
		@param min: The minimum value of the axis
		@param max: The maximum value of the axis
		@param start: The starting coordinate of the axis
		@param end: The ending coordinate of the axis
		@param majorticks: The number of major tick marks
		@type majorticks: integer
		@param minorticks: The number of minor tick marks
		@type minorticks: integer
		@param majorlength: The length of the major tick marks
		@param minorlength: The length of the minor tick marks

		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings

		@param baseid: The SVG document ID of the base line
		@type baseid: string
		@param baseclasses: Classnames to be applied to the base line
		@type baseclasses: string or sequence of strings

		@param labelidprefix: The prefix for each label ID
		@type labelidprefix: string
		@param labelclasses: Classnames to be applied to each label
		@type labelclasses: string or sequence of strings

		@param majoridprefix: The prefix for each major tick mark's ID
		@type majoridprefix: string
		@param majorclasses: Classnames to be applied to each major tick mark
		@type majorclasses: string or sequence of strings

		@param minoridprefix: The prefix for each minor tick mark's ID
		@type minoridprefix: string
		@param minorclasses: Classnames to be applied to each minor tick mark
		@type minorclasses: string or sequence of strings
		"""

		Element.__init__(self, id=id, classes=classes)

		self.majorticks = int(majorticks)
		self.minorticks = int(minorticks)

		self.baseid = baseid
		self.baseclasses = baseclasses

		self.labelidprefix = labelidprefix
		self.labelclasses = labelclasses

		self.majoridprefix = majoridprefix
		self.majorclasses = majorclasses

		self.minoridprefix = minoridprefix
		self.minorclasses = minorclasses

		self.min = float(min)
		self.max = float(max)
		self.start = float(start)
		self.end = float(end)

		self.majorlength = majorlength
		self.minorlength = minorlength

	def valueToCoord(self, value):
		"""Returns the coordinate from a value along the axis.

		@param value: A value along the axis
		"""

		return self.start + (self.end - self.start) * (value - self.min) / (self.max - self.min)

	def majorValues(self):
		"""Returns a list of the values at major tick marks."""

		return [self.min + (self.max - self.min) / (self.majorticks + 1) * x for x in xrange(1, self.majorticks + 1)]

	def majorTicks(self):
		"""Returns a list of the coordinates of major tick marks."""

		return map(self.valueToCoord, self.majorValues())

	def minorValues(self):
		"""Returns a list of the values at minor tick marks."""

		return [self.min + (self.max - self.min) / (self.minorticks + 1) * x for x in xrange(1, self.minorticks + 1)]

	def minorTicks(self):
		"""Returns a list of the coordinates of minor tick marks."""

		return map(self.valueToCoord, self.minorValues())

	def tickValues(self):
		"""Returns a sorted list of the values at all tick marks."""

		values = self.majorValues() + self.minorValues()
		values.sort()
		return values

	def tickCoords(self):
		"""Returns a sorted list of the coordinates of all tick marks."""

		return map(self.valueToCoord, self.tickValues())

	def ticks(self):
		"""Returns a list of dictionaries of the tick values and coordinates.

		The dictionaries are in the format {'value': value, 'coord', coordinate}
		"""
		
		ticklist = []
		for value, coord in zip(self.minorValues(), self.minorTicks()):
			ticklist.append({'value': value, 'coord': coord, 'type': 'minor'})

		for value, coord in zip(self.majorValues(), self.majorTicks()):
			ticklist.append({'value': value, 'coord': coord, 'type': 'major'})

		return ticklist