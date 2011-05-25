from Generator import Generator
from lib.shapes.ShapeGroup import ShapeGroup
from lib.shapes.Coordinate import Coordinate
from lib.shapes.Rectangle import Rectangle

class Scatter(Generator):
	"""Generates a scatter plot from the given data and settings."""

	def getDataField(self):
		"""Returns the datafield element."""

		id = self.settings["datafield"]["id"]
		classes = self.settings["datafield"]["class"]
		width = float(self.settings["datafield"]["width"])
		height = float(self.settings["datafield"]["height"])
		x = float(self.settings["datafield"]["x"])
		y = float(self.settings["datafield"]["y"])

		shapes = []
		try:
			border = self.settings["datafield"]["border"]
			try:
				borderid = border["id"]
			except:
				borderid = None
			try:
				borderclasses = border["class"]
			except:
				borderclasses = None
			shapes.append(Rectangle(Coordinate(x, y), width=width,
									height=height, id=borderid,
									classes=borderclasses))
		except:
			pass

		shapes.append(self.getDataSets())
		return ShapeGroup(shapes, id=id, classes=classes)


	def getDataSets(self):
		"""Returns the element containing all datasets of the chart."""

		id = self.settings["datasets"]["id"]
		classes = self.settings["datasets"]["class"]
		datasets = []
		for dataset in self.data["set"]:
			setid = dataset["id"]

			for setting in self.settings["datasets"]["set"]:
				if setting["id"] == setid:
					break

			setclasses = setting["class"]

			datasetelements = self.getDataSetElements(dataset, setting)

			datasetgroup = ShapeGroup(datasetelements, id=setid, classes=setclasses)
			datasets.append(datasetgroup)

		return ShapeGroup(datasets, id=id, classes=classes)

	def getDataSetElements(self, dataset, setting):
		"""Returns the elements which make up a particular dataset.

		@param dataset: The set of data
		@param setting: The settings of the dataset
		"""

		return self.getDataPoints(dataset, setting)

	def getDataPoints(self, dataset, setting):
		"""Returns the datapoints for a particular dataset.

		@param dataset: The set of data
		@param setting: The settings of the dataset
		"""


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
			coord = self.valueToCoord(x, y)
			point = symbol(id=u'{}-{:d}'.format(symbolidprefix, count), classes=symbolclasses)
			point.fit(symbolsize, symbolsize)
			point.translateTo(coord)
			point.translate(-symbolsize / 2, -symbolsize / 2)
			datapoints.append(point)

		return datapoints