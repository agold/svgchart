from Element import Element

class Axis(Element):

	def __init__(self, min=0.0, max=1.0, start=0.0, end=1.0,
				 majorticks=5, minorticks=20,
				 majorlength=10, minorlength=5,
				 id=u'', classes=(),
				 baseid=u'', baseclasses=(),
				 labelidprefix=u'', labelclasses=(),
				 majoridprefix=u'', majorclasses=(),
				 minoridprefix=u'', minorclasses=()):

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
		return self.start + (self.end - self.start) * (value - self.min) / (self.max - self.min)

	def majorValues(self):
		return [self.min + (self.max - self.min) / (self.majorticks + 1) * x for x in xrange(1, self.majorticks + 1)]

	def majorTicks(self):
		return map(self.valueToCoord, self.majorValues())

	def minorValues(self):
		return [self.min + (self.max - self.min) / (self.minorticks + 1) * x for x in xrange(1, self.minorticks + 1)]

	def minorTicks(self):
		return map(self.valueToCoord, self.minorValues())

	def tickValues(self):
		values = self.majorValues() + self.minorValues()
		values.sort()
		return values

	def tickCoords(self):
		return map(self.valueToCoord, self.tickValues())

	def ticks(self):
		ticklist = []
		for value, coord in zip(self.minorValues(), self.minorTicks()):
			ticklist.append({'value': value, 'coord': coord, 'type': 'minor'})

		for value, coord in zip(self.majorValues(), self.majorTicks()):
			ticklist.append({'value': value, 'coord': coord, 'type': 'major'})

		return ticklist