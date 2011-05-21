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
import argparse

parser = argparse.ArgumentParser(description='Generate an interactive SVG chart',
								 version="0.1")
parser.add_argument('--infile', '-i', action="store", dest="infile")
parser.add_argument('--settings', '-s', action="store", dest="settings")
parser.add_argument('--data', '-d', action="store", dest="data")
parser.add_argument('--scripts', '-c', action="store", dest="scripts")
parser.add_argument('--outfile', '-o', action="store", dest="outfile")
parser.add_argument('--type', '-t', action="store", dest="type", default='scatter')
parser.add_argument('--pretty', '-p', action="store_true", dest="pretty", default=False)

args = parser.parse_args()

input = InputLayer(input=args.infile,
					settings=args.settings,
					data=args.data,
					scripts=args.scripts)

parsed = ParsingLayer(input.rawInput).parsedInput

generatorname = args.type.capitalize()
genmod = __import__('lib.generators.' + generatorname, globals(), locals(), [generatorname])
generator = getattr(genmod, generatorname)

chart = generator(data=parsed.data, settings=parsed.settings)

output = SVGOutput(chart=chart.getChart(), file=args.outfile, pretty=args.pretty)
output.output()

