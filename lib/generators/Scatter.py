from Generator import Generator
from lib.elements.Legend import Legend
from lib.elements.XAxis import XAxis
from lib.elements.YAxis import YAxis
from lib.elements.HorizontalGrid import HorizontalGrid
from lib.elements.VerticalGrid import VerticalGrid
from lib.elements.Title import Title
from lib.shapes.ShapeGroup import ShapeGroup
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Shape import Shape

class Scatter(Generator):

	def __init__(self, data, settings):

		Generator.__init__(self, data, settings)
		self.__title = None
		self.__xaxis = None
		self.__yaxis = None
		self.__xgrid = None
		self.__ygrid = None
		self.__legend = None
		self.__datapoints = None
		self.__chart = None
		self.__maxvalues = None
		self.__minvalues = None

	def getChart(self):
		if self.__chart is not None:
			# Cache the chart
			return self.__chart

		id = self.settings["chart"]["id"]
		classes = self.settings["chart"]["class"]
		width = self.settings["chart"]["width"]
		height = self.settings["chart"]["height"]
		xmlns = u'http://www.w3.org/2000/svg'
		version = u'1.1'

		subelements = []
		subelements.append(self.getTitle().getElement().svg())
		subelements.append(self.getXGrid().getElement().svg())
		subelements.append(self.getYGrid().getElement().svg())
		subelements.append(self.getXAxis().getElement().svg())
		subelements.append(self.getYAxis().getElement().svg())
		subelements.append(self.getDataPoints().svg())
		subelements.append(self.getLegend().getElement().svg())

		self.__chart = Shape(tag='svg', id=id, classes=classes, subelements=subelements, attrs={'xmlns': xmlns, 'width': width, 'height': height, 'version': version})
		return self.__chart

	def getTitle(self):
		if self.__title is not None:
			# Cache the title element
			return self.__title

		if self.settings["title"]["title"].text is None:
			return None
		else:
			title = self.settings["title"]["title"].text
			titleid = self.settings["title"]["title"]["id"]
			titleclasses = self.settings["title"]["title"]["class"]

			if self.settings["title"]["subtitle"].text is not None:
				subtitle = self.settings["title"]["subtitle"].text
				subtitleid = self.settings["title"]["subtitle"]["id"]
				subtitleclasses = self.settings["title"]["subtitle"]["class"]
			else:
				subtitle = None
				subtitleid = None
				subtitleclasses = None

			x = float(self.settings["title"]["x"])
			y = float(self.settings["title"]["y"])
			width = float(self.settings["title"]["width"])
			height = float(self.settings["title"]["height"])
			id = self.settings["title"]["id"]
			classes = self.settings["title"]["class"]

			self.__title = Title(title=title, subtitle=subtitle,
					x=x, y=y, width=width, height=height,
					id=id, classes=classes,
					titleid=titleid, titleclasses=titleclasses,
					subtitleid=subtitleid, subtitleclasses=subtitleclasses)
			return self.__title

	def getXAxis(self):
		if self.__xaxis is not None:
			# Cache the x axis element
			return self.__xaxis

		id = self.settings["x-axis"]["id"]
		classes = self.settings["x-axis"]["class"]
		baseid = self.settings["x-axis"]["base"]["id"]
		baseclasses = self.settings["x-axis"]["base"]["class"]
		labelidprefix = self.settings["x-axis"]["labels"]["id-prefix"]
		labelclasses = self.settings["x-axis"]["labels"]["class"]
		majoridprefix = self.settings["x-axis"]["majors"]["id-prefix"]
		majorclasses = self.settings["x-axis"]["majors"]["class"]
		minoridprefix = self.settings["x-axis"]["minors"]["id-prefix"]
		minorclasses = self.settings["x-axis"]["minors"]["class"]

		majorticks = int(self.settings["x-axis"]["majors"]["count"])
		minorticks = int(self.settings["x-axis"]["minors"]["count"])

		majorlength = float(self.settings["x-axis"]["majors"]["size"])
		minorlength = float(self.settings["x-axis"]["minors"]["size"])

		start = 10.0 #the leftmost point. this can be made a setting somewhere to allow for some margins
		end = float(self.settings["datafield"]["width"]) + start

		ytop = 0.0 #the topmost point. this can be made a setting somewhere to allow for some margins
		y = float(self.settings["datafield"]["height"]) + ytop

		min = self.settings["x-axis"]["range"]["min"]
		max = self.settings["x-axis"]["range"]["max"]

		if min == 'auto':
			min = self.getMinValues()[0]
		else:
			min = float(min)

		if max == 'auto':
			max = self.getMaxValues()[0]
		else:
			max = float(max)

		self.__xaxis = XAxis(min=min, max=max, start=start, end=end,
				 majorticks=majorticks, minorticks=minorticks,
				 majorlength=majorlength, minorlength=minorlength,
				 y=y,
				 id=id, classes=classes,
				 baseid=baseid, baseclasses=baseclasses,
				 labelidprefix=labelidprefix, labelclasses=labelclasses,
				 majoridprefix=majoridprefix, majorclasses=majorclasses,
				 minoridprefix=minoridprefix, minorclasses=minorclasses)
		return self.__xaxis

	def getYAxis(self):
		if self.__yaxis is not None:
			# Cache the y axis element
			return self.__yaxis

		id = self.settings["y-axis"]["id"]
		classes = self.settings["y-axis"]["class"]
		baseid = self.settings["y-axis"]["base"]["id"]
		baseclasses = self.settings["y-axis"]["base"]["class"]
		labelidprefix = self.settings["y-axis"]["labels"]["id-prefix"]
		labelclasses = self.settings["y-axis"]["labels"]["class"]
		majoridprefix = self.settings["y-axis"]["majors"]["id-prefix"]
		majorclasses = self.settings["y-axis"]["majors"]["class"]
		minoridprefix = self.settings["y-axis"]["minors"]["id-prefix"]
		minorclasses = self.settings["y-axis"]["minors"]["class"]

		majorticks = int(self.settings["y-axis"]["majors"]["count"])
		minorticks = int(self.settings["y-axis"]["minors"]["count"])

		majorlength = float(self.settings["y-axis"]["majors"]["size"])
		minorlength = float(self.settings["y-axis"]["minors"]["size"])

		start = 0.0 #the topmost point. this can be made a setting somewhere to allow for some margins
		end = float(self.settings["datafield"]["height"]) + start

		xleft = 0.0 #the leftmost point. this can be made a setting somewhere to allow for some margins

		min = self.settings["y-axis"]["range"]["min"]
		max = self.settings["y-axis"]["range"]["max"]

		if min == 'auto':
			min = self.getMinValues()[1]
		else:
			min = float(min)

		if max == 'auto':
			max = self.getMaxValues()[1]
		else:
			max = float(max)



		self.__yaxis = YAxis(min=min, max=max, start=start, end=end,
				 majorticks=majorticks, minorticks=minorticks,
				 majorlength=majorlength, minorlength=minorlength,
				 x=xleft,
				 id=id, classes=classes,
				 baseid=baseid, baseclasses=baseclasses,
				 labelidprefix=labelidprefix, labelclasses=labelclasses,
				 majoridprefix=majoridprefix, majorclasses=majorclasses,
				 minoridprefix=minoridprefix, minorclasses=minorclasses)
		return self.__yaxis

	def getAxes(self):
		return [self.getXAxis().getElement(), self.getYAxis().getElement()]

	def getXGrid(self):
		if self.__xgrid is not None:
			# Cache the x grid element
			return self.__xgrid

		points = self.getXAxis().majorTicks()
		top = 0.0 #the topmost point. this can be made a setting somewhere to allow for some margins
		bottom = float(self.settings["datafield"]["height"]) + top
		id = self.settings["x-axis"]["grid"]["id"]
		classes = self.settings["x-axis"]["grid"]["class"]
		lineidprefix = self.settings["x-axis"]["grid"]["lines"]["id-prefix"]
		lineclasses = self.settings["x-axis"]["grid"]["lines"]["class"]

		self.__xgrid = VerticalGrid(points=points, top=top, bottom=bottom,
				id=id, classes=classes,
				lineidprefix=lineidprefix, lineclasses=lineclasses)
		return self.__xgrid

	def getYGrid(self):
		if self.__ygrid is not None:
			# Cache the y grid element
			return self.__ygrid

		points = self.getYAxis().majorTicks()
		left = 0.0 #the leftmost point. this can be made a setting somewhere to allow for some margins
		right = float(self.settings["datafield"]["width"]) + left
		id = self.settings["y-axis"]["grid"]["id"]
		classes = self.settings["y-axis"]["grid"]["class"]
		lineidprefix = self.settings["y-axis"]["grid"]["lines"]["id-prefix"]
		lineclasses = self.settings["y-axis"]["grid"]["lines"]["class"]

		self.__ygrid = HorizontalGrid(points=points, left=left, right=right,
				id=id, classes=classes,
				lineidprefix=lineidprefix, lineclasses=lineclasses)
		return self.__ygrid

	def getGrid(self):
		return [self.getXGrid().getElement(), self.getYGrid().getElement()]

	def getLegend(self):
		if self.__legend is not None:
			# Cache the legend element
			return self.__legend

		entries = []
		for dataset in self.settings["datasets"]["set"]:
			shapename = dataset["symbol"]["shape"].capitalize()
			label = dataset["label"]
			shape = __import__('lib.shapes.' + shapename, globals(), locals(), [shapename])
			entry = {'shape': getattr(shape, shapename)(), 'text': label}
			entries.append(entry)

		x = float(self.settings["legend"]["x"])
		y = float(self.settings["legend"]["y"])
		width = float(self.settings["legend"]["width"])
		entryheight = float(self.settings["legend"]["entries"]["height"])
		title = self.settings["legend"]["title"].text
		titlesize = float(self.settings["legend"]["title"]["size"])
		id = self.settings["legend"]["id"]
		classes = self.settings["legend"]["class"]
		titleid = self.settings["legend"]["title"]["id"]
		titleclasses = self.settings["legend"]["title"]["class"]
		entryidprefix = self.settings["legend"]["entries"]["id-prefix"]
		entryclasses = self.settings["legend"]["entries"]["class"]
		entryshapeprefix = self.settings["legend"]["entries"]["shapes"]["id-prefix"]
		entryshapeclasses = self.settings["legend"]["entries"]["shapes"]["class"]
		entrytextprefix = self.settings["legend"]["entries"]["labels"]["id-prefix"]
		entrytextclasses = self.settings["legend"]["entries"]["labels"]["class"]

		self.__legend = Legend(entries=entries, x=x, y=y,
				width=width, entryheight=entryheight,
				title=title, titlesize=titlesize,
				id=id, classes=classes,
				titleid=titleid, titleclasses=titleclasses,
				entryidprefix=entryidprefix, entryclasses=entryclasses,
				entryshapeprefix=entryshapeprefix, entryshapeclasses=entryshapeclasses,
				entrytextprefix=entrytextprefix, entrytextclasses=entrytextclasses)
		return self.__legend

	def getMaxValues(self):
		if self.__maxvalues is not None:
			# Cache the max value
			return self.__maxvalues

		maxx = None
		maxy = None
		for dataset in self.data["set"]:
			for value in dataset["value"]:
				if float(value["x"]) > maxx:
					maxx = float(value["x"])
				if float(value["y"]) > maxy:
					maxy = float(value["y"])
		self.__maxvalues = (maxx, maxy)
		return self.__maxvalues

	def getMinValues(self):
		if self.__minvalues is not None:
			# Cache the min value
			return self.__minvalues

		minx = self.getMaxValues()[0]
		miny = self.getMaxValues()[1]
		for dataset in self.data["set"]:
			for value in dataset["value"]:
				if float(value["x"]) < minx:
					minx = float(value["x"])
				if float(value["y"]) < miny:
					miny = float(value["y"])
		self.__minvalues = (minx, miny)
		return self.__minvalues

	def getDataPoints(self):
		if self.__datapoints is not None:
			# Cache the datapoints element
			return self.__datapoints

		def valueToCoord(x, y):
			return Coordinate(self.getXAxis().valueToCoord(x),
							  self.getYAxis().valueToCoord(y))

		id = self.settings["datasets"]["id"]
		classes = self.settings["datasets"]["class"]
		datasets = []
		for dataset in self.data["set"]:
			setid = dataset["id"]

			for setting in self.settings["datasets"]["set"]:
				if setting["id"] == setid:
					break

			setclasses = setting["class"]
			symbolsize = float(setting["symbol"]["size"])
			shapename = setting["symbol"]["shape"].capitalize()
			shapemodule = __import__('lib.shapes.' + shapename, globals(), locals(), [shapename])
			symbol = getattr(shapemodule, shapename)

			symbolidprefix = setting["symbol"]["id-prefix"]
			symbolclasses = setting["symbol"]["class"]

			datapoints = []
			count = 0
			for value in dataset["value"]:
				count += 1

				x = float(value["x"])
				y = float(value["y"])
				coord = valueToCoord(x, y)
				point = symbol(id=u'{}-{:d}'.format(symbolidprefix, count), classes=symbolclasses)
				point.fit(symbolsize, symbolsize)
				point.translateTo(coord)
				datapoints.append(point)

			datasetgroup = ShapeGroup(datapoints, id=setid, classes=setclasses)
			datasets.append(datasetgroup)

		self.__datapoints = ShapeGroup(datasets, id=id, classes=classes)
		return self.__datapoints


