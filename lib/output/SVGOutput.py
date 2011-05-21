import sys
try:
	import xml.etree.cElementTree as etree
except:
	import xml.etree.ElementTree as etree

class SVGOutput(object):
	"""Outputs a chart to the given file or standard output."""

	def __init__(self, chart=None, file=None, pretty=False):
		"""
		@param chart: The chart to print.
		@type chart: Shape
		@param file: The file to print to. Defaults to sys.stdout
		@param pretty: Enables pretty-printed XML. This option will use the minidom module and may degrade performance significantly.
		@type pretty: Boolean
		"""

		self.chart = chart
		self.pretty = pretty
		self.file = file or sys.stdout

	def output(self):
		"""Outputs the chart."""
		
		if self.pretty:
			from xml.dom.minidom import parseString
			with open(self.file, 'w') as f:
				f.write(parseString(str(self.chart)).toprettyxml(encoding="utf-8"))
		else:
			chart = etree.ElementTree(self.chart.svg())
			chart.write(self.file, encoding="utf-8", default_namespace=False, xml_declaration=True, method="xml")