"""Main interface to svgchart.

usage: svgchart.py [-h] [-v] [--infile INFILE] [--settings SETTINGS]
                   [--data DATA] [--scripts SCRIPTS] [--outfile OUTFILE]
                   [--type TYPE] [-pretty]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --infile INFILE, -i INFILE
  --settings SETTINGS, -s SETTINGS
  --data DATA, -d DATA
  --scripts SCRIPTS, -c SCRIPTS
  --outfile OUTFILE, -o OUTFILE
  --type TYPE, -t TYPE
  -pretty, -p

"""

from lib.input.InputLayer import InputLayer
from lib.parse.ParsingLayer import ParsingLayer
from lib.output.SVGOutput import SVGOutput

def getChart(infile, settings, data, scripts, outfile, type, pretty):
	input = InputLayer(input=infile,
					settings=settings,
					data=data,
					scripts=scripts)

	parsed = ParsingLayer(input.rawInput).parsedInput

	generatorname = type.capitalize()
	genmod = __import__('lib.generators.' + generatorname, globals(), locals(), [generatorname])
	generator = getattr(genmod, generatorname)

	chart = generator(data=parsed.data, settings=parsed.settings)

	output = SVGOutput(chart=chart.getChart(), file=outfile, pretty=pretty)
	output.output()

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(description='Generate an interactive SVG chart',
									 version="0.1")
	parser.add_argument('-i', '--infile', action="store", dest="infile", help="File containing settings, data, and scripts")
	parser.add_argument('-s', '--settings', action="store", dest="settings", help="File containing the chart settings")
	parser.add_argument('-d', '--data', action="store", dest="data", help="File containing the chart data")
	parser.add_argument('-c', '--scripts', action="store", dest="scripts", help="File containing the chart scripts")
	parser.add_argument('-o', '--outfile', action="store", dest="outfile", help="Output file")
	parser.add_argument('-t', '--type', action="store", dest="type", default="scatter", help="Type of chart to generate")
	parser.add_argument('-p', '--pretty', action="store_true", dest="pretty", default=False, help="Pretty print the XML output")

	args = parser.parse_args()

	getChart(args.infile, args.settings, args.data, args.scripts,
			 args.outfile, args.type, args.pretty)

