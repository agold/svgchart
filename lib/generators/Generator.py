from lib.elements.Legend import Legend
from lib.elements.XAxis import XAxis
from lib.elements.YAxis import YAxis
from lib.elements.HorizontalGrid import HorizontalGrid
from lib.elements.VerticalGrid import VerticalGrid
from lib.elements.Title import Title
from lib.shapes.Shape import Shape
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Rectangle import Rectangle
import re
import json

class Generator(object):
	"""Base class for a chart generator."""

	def __init__(self, data, settings, scripts):
		"""
		@param data: The parsed data to create the chart from
		@param settings: The settings used to format the chart
		@param scripts: The scripts to be included in the chart
		"""

		self.data = data
		self.settings = settings
		self.scripts = scripts
		self.styles = {}

		self.__title = None
		self.__xaxis = None
		self.__yaxis = None
		self.__xgrid = None
		self.__ygrid = None
		self.__legend = None
		self.__chart = None
		self.__maxvalues = None
		self.__minvalues = None

	def getChart(self):
		"""Assembles all of the elements and returns them in an svg tag."""

		if self.__chart is not None:
			# Cache the chart
			return self.__chart

		id = self.settings["chart"]["id"]
		classes = self.settings["chart"]["class"]
		width = float(self.settings["chart"]["width"])
		height = float(self.settings["chart"]["height"])
		xmlns = u'http://www.w3.org/2000/svg'
		version = u'1.1'

		subelements = []
		subelements.append(self.getCSS().svg())
		subelements.extend(self.getScripts())
		try:
			border = self.settings["chart"]["border"]
			try:
				borderid = border["id"]
			except:
				borderid = None
			try:
				borderclasses = border["class"]
			except:
				borderclasses = None
			subelements.append(Rectangle(Coordinate(0, 0), width=width - 1,
									height=height - 1, id=borderid,
									classes=borderclasses).svg())
		except:
			pass

		subelements.append(self.getTitle().getElement().svg())
		subelements.append(self.getXGrid().getElement().svg())
		subelements.append(self.getYGrid().getElement().svg())
		subelements.append(self.getXAxis().getElement().svg())
		subelements.append(self.getYAxis().getElement().svg())
		if self.getDataField():
			subelements.append(self.getDataField().svg())
		subelements.append(self.getLegend().getElement().svg())

		self.__chart = Shape(tag='svg', id=id, classes=classes, subelements=subelements, attrs={'xmlns': xmlns, 'width': width, 'height': height, 'version': version})
		return self.__chart

	def getDataField(self):
		return None
	
	def getTitle(self):
		"""Returns the title element of the chart."""

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

			try:
				border = self.settings["title"]["border"]
				enableborder = True
				try:
					borderid = border["id"]
				except:
					borderid = None
				try:
					borderclasses = border["class"]
				except:
					borderclasses = None
			except:
				enableborder = False
				borderid = None
				borderclasses = None


			self.__title = Title(title=title, subtitle=subtitle,
					x=x, y=y, width=width, height=height,
					id=id, classes=classes,
					titleid=titleid, titleclasses=titleclasses,
					subtitleid=subtitleid, subtitleclasses=subtitleclasses,
					border=enableborder, borderid=borderid, borderclasses=borderclasses)
			return self.__title

	def getXAxis(self):
		"""Returns the x-axis element of the chart."""

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

		start = float(self.settings["datafield"]["x"]) #the leftmost point. this can be made a setting somewhere to allow for some margins
		end = float(self.settings["datafield"]["width"]) + start

		ytop = float(self.settings["datafield"]["y"]) #the topmost point. this can be made a setting somewhere to allow for some margins
		y = float(self.settings["datafield"]["height"]) + ytop

		labelformat = self.settings["y-axis"]["labels"]["format"]

		min = self.settings["x-axis"]["range"]["min"]
		max = self.settings["x-axis"]["range"]["max"]

		if min == 'auto':
			min = self.getMinValues()[0] - (self.getMaxValues()[0] - self.getMinValues()[0]) * 0.1
		else:
			min = float(min)

		if max == 'auto':
			max = self.getMaxValues()[0] + (self.getMaxValues()[0] - self.getMinValues()[0]) * 0.1
		else:
			max = float(max)

		self.__xaxis = XAxis(min=min, max=max, start=start, end=end,
				 majorticks=majorticks, minorticks=minorticks,
				 majorlength=majorlength, minorlength=minorlength,
				 y=y, labelformat=labelformat,
				 id=id, classes=classes,
				 baseid=baseid, baseclasses=baseclasses,
				 labelidprefix=labelidprefix, labelclasses=labelclasses,
				 majoridprefix=majoridprefix, majorclasses=majorclasses,
				 minoridprefix=minoridprefix, minorclasses=minorclasses)
		return self.__xaxis

	def getYAxis(self):
		"""Returns the y-axis element of the chart."""

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

		start = float(self.settings["datafield"]["y"]) #the topmost point. this can be made a setting somewhere to allow for some margins
		end = float(self.settings["datafield"]["height"]) + start

		labelformat = self.settings["y-axis"]["labels"]["format"]

		xleft = float(self.settings["datafield"]["x"]) #the leftmost point. this can be made a setting somewhere to allow for some margins

		min = self.settings["y-axis"]["range"]["min"]
		max = self.settings["y-axis"]["range"]["max"]

		if min == 'auto':
			min = self.getMinValues()[1] - (self.getMaxValues()[1] - self.getMinValues()[1]) * 0.1
		else:
			min = float(min)

		if max == 'auto':
			max = self.getMaxValues()[1] + (self.getMaxValues()[1] - self.getMinValues()[1]) * 0.1
		else:
			max = float(max)



		self.__yaxis = YAxis(min=min, max=max, start=start, end=end,
				 majorticks=majorticks, minorticks=minorticks,
				 majorlength=majorlength, minorlength=minorlength,
				 x=xleft, labelformat=labelformat,
				 id=id, classes=classes,
				 baseid=baseid, baseclasses=baseclasses,
				 labelidprefix=labelidprefix, labelclasses=labelclasses,
				 majoridprefix=majoridprefix, majorclasses=majorclasses,
				 minoridprefix=minoridprefix, minorclasses=minorclasses)
		return self.__yaxis

	def getAxes(self):
		return [self.getXAxis().getElement(), self.getYAxis().getElement()]

	def getXGrid(self):
		"""Returns the x-axis grid for the chart."""

		if self.__xgrid is not None:
			# Cache the x grid element
			return self.__xgrid

		points = self.getXAxis().majorTicks()
		start = self.getXAxis().start
		end = self.getXAxis().end
		top = float(self.settings["datafield"]["y"])
		bottom = float(self.settings["datafield"]["height"]) + top
		id = self.settings["x-axis"]["grid"]["id"]
		classes = self.settings["x-axis"]["grid"]["class"]
		lineidprefix = self.settings["x-axis"]["grid"]["lines"]["id-prefix"]
		lineclasses = self.settings["x-axis"]["grid"]["lines"]["class"]

		self.__xgrid = VerticalGrid(points=points, top=top, bottom=bottom,
				start=start, end=end,
				id=id, classes=classes,
				lineidprefix=lineidprefix, lineclasses=lineclasses)
		return self.__xgrid

	def getYGrid(self):
		"""Returns the y-axis grid for the chart."""

		if self.__ygrid is not None:
			# Cache the y grid element
			return self.__ygrid

		points = self.getYAxis().majorTicks()
		start = self.getYAxis().start
		end = self.getYAxis().end
		left = float(self.settings["datafield"]["x"])
		right = float(self.settings["datafield"]["width"]) + left
		id = self.settings["y-axis"]["grid"]["id"]
		classes = self.settings["y-axis"]["grid"]["class"]
		lineidprefix = self.settings["y-axis"]["grid"]["lines"]["id-prefix"]
		lineclasses = self.settings["y-axis"]["grid"]["lines"]["class"]

		self.__ygrid = HorizontalGrid(points=points, left=left, right=right,
				start=start, end=end,
				id=id, classes=classes,
				lineidprefix=lineidprefix, lineclasses=lineclasses)
		return self.__ygrid

	def getGrid(self):
		"""Returns a list of both grid elements."""

		return [self.getXGrid().getElement(), self.getYGrid().getElement()]

	def getLegend(self):
		"""Returns the chart's legend element."""

		if self.__legend is not None:
			# Cache the legend element
			return self.__legend

		entries = self.settings["datasets"]["set"]


		x = float(self.settings["legend"]["x"])
		y = float(self.settings["legend"]["y"])
		width = float(self.settings["legend"]["width"])
		height = float(self.settings["legend"]["height"])
		entryheight = float(self.settings["legend"]["entries"]["height"])
		title = self.settings["legend"]["title"].text
		titlesize = float(self.settings["legend"]["title"]["size"])
		id = self.settings["legend"]["id"]
		classes = self.settings["legend"]["class"]
		titleid = self.settings["legend"]["title"]["id"]
		titleclasses = self.settings["legend"]["title"]["class"]

		try:
			border = self.settings["legend"]["border"]
			enableborder = True
			try:
				borderid = border["id"]
			except:
				borderid = None
			try:
				borderclasses = border["class"]
			except:
				borderclasses = None
		except:
			enableborder = False
			borderid = None
			borderclasses = None
		
		self.__legend = Legend(entries=entries, x=x, y=y,
				width=width, height=height, entryheight=entryheight,
				title=title, titlesize=titlesize,
				id=id, classes=classes,
				titleid=titleid, titleclasses=titleclasses,
				border=enableborder, borderid=borderid, borderclasses=borderclasses)
		return self.__legend

	def getCSS(self):
		"""Returns a style element containing the style rules given in the settings document."""

		self.getStyles()
		return Shape(tag=u'style', text=self.CSSString(), attrs={u'type': u'text/css'})

	def CSSString(self):
		"""Collects all of the style strings."""

		cssstrings = []
		for key in self.styles:
			styles = self.styles[key]
			stylestrings = []
			for stylekey in styles:
				stylestrings.append(': '.join([stylekey, styles[stylekey]]))
			stylestring = '; '.join(stylestrings)
			cssstrings.append('{key} {{ {style}; }}'.format(key=key, style=stylestring))
		return "\n".join(cssstrings)


	def getStyles(self, section=None):
		"""Recursively retrieves the style information from a given section of the settings document.

		@param section: The section to search through
		"""

		if section is None:
			section = self.settings
		for setting in section:
			try:
				style = setting["style"]
				try:
					id = setting["id"]
					self.addStyleToId(id, style)
				except:
					classname = setting["class"]
					self.addStyleToClass(classname, style)
			except:
				pass
			for subsetting in setting:
				if isinstance(subsetting, list):
					self.getStyles(subsetting)
		return self.styles

	def getScripts(self):
		scripts = []
		for script in self.scripts["script"]:
			id = script["id"]
			try:
				scriptfile = script["file"]
				scripttext = open(scriptfile, 'r').read()
			except:
				scripttext = script.text

			parsed = self.parseScript(scripttext)
			scriptelem = Shape(tag=u'script', cdata=parsed, id=id, attrs={u'type': u'text/ecmascript'})
			scripts.append(scriptelem.svg())
		return scripts

	def addStyleToClass(self, classname=u'', style=u''):
		"""Applies a style to a given class name.

		@param classname: The classname to apply to
		@param style: The style string
		"""

		classes = []
		for oneclass in classname.split():
			valid = re.match(r'^-?[_a-zA-Z]+[_a-zA-Z0-9-]*$', oneclass)
			if valid:
				classes.append('.' + oneclass)

		self.styles[', '.join(classes)] = self.parseStyle(style)

	def addStyleToId(self, id=u'', style=u''):
		"""Applies a style to a given ID tag.

		@param id: The ID to apply to
		@param style: The style string
		"""

		valid = re.match(r'^[a-zA-Z][-a-zA-Z0-9_:\.]*$', id)
		if valid:
			self.styles['#' + id] = self.parseStyle(style)

	def addStyleToTag(self, tag, style):
		"""Applies a style to a given tag name.

		@param tag: The tag name to apply to
		@param style: The style string
		"""

		valid = re.match(r'^[a-zA-Z_:][-a-zA-Z0-9_:\.]*$', tag)
		if valid:
			self.styles[tag] = self.parseStyle(style)

	def parseStyle(self, style=''):
		"""Parses a style string into its constituent key:value pairs.

		@param style: The style string to parse
		"""

		styles = style.split(';')
		styledict = {}
		for pair in styles:
			if len(pair) > 0:
				key, value = pair.split(':')
				styledict[key.strip()] = value.strip()

		return styledict

	def getJSONDataSets(self):
		datasets = {}
		for dataset in self.data["set"]:
			setid = dataset["id"]

			for setting in self.settings["datasets"]["set"]:
				if setting["id"] == setid:
					break

			idprefix = setting["symbol"]["id-prefix"]
			values = []
			count = 0
			for value in dataset["value"]:
				count += 1
				valx = float(value["x"])
				valy = float(value["y"])
				coord = self.valueToCoord(valx, valy)
				valuedict = {"val": {"x": valx, "y": valy},
							 "coord": {"x": coord.x, "y": coord.y},
							 "id": "{}-{:d}".format(idprefix, count)}
				values.append(valuedict)
			datasets[setid] = values
		return json.dumps(datasets, separators=(', ', ': '))

	def parseScript(self, script=u''):
		script = unicode(script)
		script = re.sub(u"\{", u"%!%", script)
		script = re.sub(u"\}", u"%#%", script)
		script = re.sub(u"%%([^%]+)%%", u"{\\1}", script)

		parsed = script.format(settings=self.settings, datasets=self.getJSONDataSets())

		parsed = re.sub(u"%!%", u"{", parsed)
		parsed = re.sub(u"%#%", u"}", parsed)
		return parsed

	def getMaxValues(self):
		"""Returns the maximum x and y values of the chart's data."""

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
		"""Returns the minimum x and y values of the chart's data."""

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

	def valueToCoord(self, x, y):
		"""Returns a Coordinate from the given x and y values.

		@param x: The x value
		@param y: The y value
		"""

		return Coordinate(self.getXAxis().valueToCoord(x),
						  self.getYAxis().valueToCoord(y))
