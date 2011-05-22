from Scatter import Scatter
from lib.shapes.Path import Path

class Line(Scatter):
	"""Adds a line connecting the data points of a scatter plot in order."""

	def getDataSetElements(self, dataset, setting):
		"""Adds a data line to the dataset.
		The line is made the first element so the data points are rendered in front.

		"""

		elements = Scatter.getDataSetElements(self, dataset, setting)
		elements.insert(0, self.getDataLine(dataset, setting))

		return elements

	def getDataLine(self, dataset, setting):
		"""Returns a path element connecting the data points.

		@param dataset: The set of data to connect
		@param setting: The settings of the dataset
		"""

		id = setting["line"]["id"]
		classes = setting["line"]["class"]

		vertices = []
		for value in dataset["value"]:
			x = float(value["x"])
			y = float(value["y"])
			coord = self.valueToCoord(x, y)
			vertices.append(coord)

		return Path(coordinates=vertices, id=id, classes=classes)
