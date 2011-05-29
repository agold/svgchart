import sys
import gzip
import lib.ElementTreeCDATA as etree

class SVGOutput(object):
	"""Outputs a chart to the given file or standard output."""

	def __init__(self, chart=None, outfile=None, pretty=False):
		"""
		@param chart: The chart to print.
		@type chart: Shape
		@param outfile: The file to print to. Defaults to sys.stdout
		@param pretty: Enables pretty-printed XML. This option will use the minidom module and may degrade performance significantly.
		@type pretty: Boolean
		"""

		self.chart = chart
		self.pretty = pretty

		if isinstance(outfile, file) or hasattr(outfile, 'write'):
			self.outfile = outfile
		elif not outfile:
			self.outfile = sys.stdout
		elif outfile[-5:] == '.svgz':
			self.outfile = gzip.open(outfile, 'wb')
		else:
			self.outfile = open(outfile, 'w')

	def output(self):
		"""Outputs the chart."""
		
		if self.pretty:
			from xml.dom.minidom import parseString
			self.outfile.write(parseString(str(self.chart)).toprettyxml(encoding="utf-8"))
		else:
			chart = etree.ElementTree(self.chart.svg())
			chart.write(self.outfile, encoding="utf-8", default_namespace=False, xml_declaration=True, method="xml")