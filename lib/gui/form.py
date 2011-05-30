from lib.input.InputSet import InputSet
from lib.input.FileInput import FileInput
import lib.parse.ParsedInput as ParsedInput
from lib.parse.IndexedDict import IndexedDict

def getGUI(f):
	"""Writes an HTML GUI to f.
	@param f: File to write to
	"""
	header(f)
	initColors(f,['red','green','blue','yellow'])
	initTabs(f,['settings','data','scripts','submission'])
	openForm(f)
	settingsPage(f)
	dataPage(f)
	scriptsPage(f)
	submissionPage(f)
	closeForm(f)
	footer(f)

def header(f):
	"""Writes the opening section of the GUI.
	@param f: File to write to
	"""
	f.write("""
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
		<html>
		<head>
			<title>SVGChart GUI</title>
	""")
	style(f)
	tabScript(f)
	f.write("""
		</head>
		<body onload='init_tabs()'>
	""")

def style(f):
	"""Writes the CSS style section of the GUI.
	@param f: File to write to
	"""
	f.write("<style type='text/css'>")
	with open('lib/gui/style.css','r') as stylesheet:
		f.write(stylesheet.read())
	f.write("</style>")

def tabScript(f):
	"""Writes the tabbing script for the GUI.
	@param f: File to write to
	"""
	openScript(f)
	f.write("""
		if (!Array.indexOf) {
			Array.prototype.indexOf = function (obj) {
				for (var i = 0;i < this.length;i++)
					if (this[i] == obj)
						return i;
				return -1;
			}
		}
		var colors = new Array()
		var tabs = new Array()
		var pages = new Array()
		function init_tabs() {
			for (var i = 0;i < pages.length;i++)
				pages[i].className = colors[i] + ' page'
			select_tab(tabs[0])
		}
		function reset_tabs() {
			for (var i = 0;i < tabs.length;i++) {
				tabs[i].className = colors[i] + ' tab'
				pages[i].style.display = 'none'
			}
		}
		function select_tab(tab) {
			reset_tabs()
			var index = tabs.indexOf(tab)
			var page = pages[index]
			tab.className = tab.className + ' selected'
			page.style.display = 'block'
		}
	""")
	closeScript(f)

def initColors(f,colors):
	"""Writes a script section to initialize the tab colors for the GUI.
	@param f: File to write to
	@param colors: List of color names
	"""
	openScript(f)
	for color in colors:
		f.write("colors.push('" + color + "')\n")
	closeScript(f)

def initTabs(f,labels):
	"""Initializes the tabs for the GUI.
	@param f: File to write to
	@param labels: List of tab labels
	"""
	for label in labels:
		f.write("<span id='" + label + "tab' onclick='select_tab(this)'>" + label.capitalize() + "</span>")
		openScript(f)
		f.write("tabs.push(document.getElementById('" + label + "tab'))")
		closeScript(f)

def openForm(f):
	"""Initializes the form for the GUI.
	@param f: File to write to
	"""
	f.write("<form enctype='multipart/form-data' action='.' method='post' style='display:inline;'>")

def settingsPage(f):
	"""Writes the settings page for the GUI.
	@param f: File to write to
	"""
	openPage(f,'settings')

	# Obtain defaults
	settingsinput = InputSet('settings')
	FileInput([settingsinput],'defaults/default.scatter.settings.xml')
	settings = IndexedDict()
	ParsedInput.parseXml(settingsinput.textlist[0],settings)

	f.write("""
		<fieldset><legend>Type</legend>
			<input type='radio' name='type' value='scatter' checked='checked' /> Scatter
			<input type='radio' name='type' value='line' /> Line
		</fieldset>
		<fieldset><legend>Chart Area</legend>
			<table>
				<tr>
					<td>Size:</td>
					<td><input type='text' name='/chart@width' value='""" + settings['chart']['width'] + """' /> x
						<input type='text' name='/chart@height' value='""" + settings['chart']['height'] + """' /></td>
				</tr><tr>
					<td>Background:</td>
					<td><input type='text' name='/chart/border@style$fill' value='none' /></td>
				</tr><tr>
					<td>Border Color:</td>
					<td><input type='text' name='/chart/border@style$stroke' value='black' /></td>
				</tr><tr>
					<td>Border Width:</td>
					<td><input type='text' name='/chart/border@style$stroke-width' value='1px' /> (pixels--please end with "px")</td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Title</legend>
			<table>
				<tr>
					<td>Title:</td>
					<td><input type='text' name='/title/title' value='""" + (settings['title']['title'].text or "") + """' /></td>
				</tr><tr>
					<td>Subtitle:</td>
					<td><input type='text' name='/title/subtitle' value='""" + (settings['title']['subtitle'].text or "") + """' /></td>
				</tr><tr>
					<td>Size:</td>
					<td><input type='text' name='/title@width' value='""" + settings['title']['width'] + """' /> x
						<input type='text' name='/title@height' value='""" + settings['title']['height'] + """' /></td>
				</tr><tr>
					<td>Location:</td>
					<td><input type='text' name='/title@x' value='""" + settings['title']['x'] + """' /> ,
						<input type='text' name='/title@y' value='""" + settings['title']['y'] + """' /> (top left corner coordinates)</td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>X-Axis</legend>
			<table>
				<tr>
					<td>Major Tick Number:</td>
					<td><input type='text' name='/x-axis/majors@count' value='""" + settings['x-axis']['majors']['count'] + """' /></td>
				</tr><tr>
					<td>Major Tick Size:</td>
					<td><input type='text' name='/x-axis/majors@size' value='""" + settings['x-axis']['majors']['size'] + """' /></td>
				</tr><tr>
					<td>Minor Tick Number:</td>
					<td><input type='text' name='/x-axis/minors@count' value='""" + settings['x-axis']['minors']['count'] + """' /></td>
				</tr><tr>
					<td>Minor Tick Size:</td>
					<td><input type='text' name='/x-axis/minors@size' value='""" + settings['x-axis']['minors']['size'] + """' /></td>
				</tr><tr>
					<td>Label Format:</td>
					<td><input type='text' name='/x-axis/labels@format' value='""" + settings['x-axis']['labels']['format'] + """' /> (e.g. %d for integer, %.2f for 2 decimal places)</td>
				</tr><tr>
					<td>Range Min:</td>
					<td><input type='text' name='/x-axis/range@min' value='""" + settings['x-axis']['range']['min'] + """' /></td>
				</tr><tr>
					<td>Range Max:</td>
					<td><input type='text' name='/x-axis/range@max' value='""" + settings['x-axis']['range']['max'] + """' /></td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Y-Axis</legend>
			<table>
				<tr>
					<td>Major Tick Number:</td>
					<td><input type='text' name='/y-axis/majors@count' value='""" + settings['y-axis']['majors']['count'] + """' /></td>
				</tr><tr>
					<td>Major Tick Size:</td>
					<td><input type='text' name='/y-axis/majors@size' value='""" + settings['y-axis']['majors']['size'] + """' /></td>
				</tr><tr>
					<td>Minor Tick Number:</td>
					<td><input type='text' name='/y-axis/minors@count' value='""" + settings['y-axis']['minors']['count'] + """' /></td>
				</tr><tr>
					<td>Minor Tick Size:</td>
					<td><input type='text' name='/y-axis/minors@size' value='""" + settings['y-axis']['minors']['size'] + """' /></td>
				</tr><tr>
					<td>Label Format:</td>
					<td><input type='text' name='/y-axis/labels@format' value='""" + settings['y-axis']['labels']['format'] + """' /> (e.g. %d for integer, %.2f for 2 decimal places)</td>
				</tr><tr>
					<td>Range Min:</td>
					<td><input type='text' name='/y-axis/range@min' value='""" + settings['y-axis']['range']['min'] + """' /></td>
				</tr><tr>
					<td>Range Max:</td>
					<td><input type='text' name='/y-axis/range@max' value='""" + settings['y-axis']['range']['max'] + """' /></td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Data Area</legend>
			<table>
				<tr>
					<td>Size:</td>
					<td><input type='text' name='/datafield@width' value='""" + settings['datafield']['width'] + """' /> x
						<input type='text' name='/datafield@height' value='""" + settings['datafield']['height'] + """' /></td>
				</tr><tr>
					<td>Location:</td>
					<td><input type='text' name='/datafield@x' value='""" + settings['datafield']['x'] + """' /> ,
						<input type='text' name='/datafield@y' value='""" + settings['datafield']['y'] + """' /> (top left corner coordinates)</td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Dataset</legend>
			<table>
				<tr>
					<td>Symbol:</td>
					<td>Shape:</td>
					<td><input type='radio' name='/datasets/set/symbol@shape' value='circle' checked='checked' /> Circle
						<input type='radio' name='/datasets/set/symbol@shape' value='square' /> Square</td>
				</tr><tr>
					<td></td>
					<td>Size:</td>
					<td><input type='text' name='/datasets/set/symbol@size' value='""" + settings['datasets']['set']['symbol']['size'] + """' /></td>
				</tr><tr>
					<td></td>
					<td>Color:</td>
					<td><input type='text' name='/datasets/set/symbol@style$fill,/datasets/set/legend-entry/symbol@style$fill' value='green' /></td>
				</tr><tr>
					<td>Line:</td>
					<td>Color:</td>
					<td><input type='text' name='/datasets/set/line@style$stroke' value='green' /></td>
				</tr><tr>
					<td></td>
					<td>Width:</td>
					<td><input type='text' name='/datasets/set/line@style$stroke-width' value='1px' /> (pixels--please end with "px")</td>
				</tr>
			</table>
			<input type='hidden' name='/datasets/set/line@style$fill' value='none' />
		</fieldset>
		<fieldset><legend>Legend</legend>
			<table>
				<tr>
					<td>Size:</td>
					<td><input type='text' name='/legend@width' value='""" + settings['legend']['width'] + """' /> x
						<input type='text' name='/legend@height' value='""" + settings['legend']['height'] + """' /></td>
				</tr><tr>
					<td>Location:</td>
					<td><input type='text' name='/legend@x' value='""" + settings['legend']['x'] + """' /> ,
						<input type='text' name='/legend@y' value='""" + settings['legend']['y'] + """' /> (top left corner coordinates)</td>
				</tr><tr>
					<td>Title:</td>
					<td><input type='text' name='/legend/title' value='""" + (settings['legend']['title'].text or "") + """' /></td>
				</tr><tr>
					<td>Title Size:</td>
					<td><input type='text' name='/legend/title@size' value='""" + settings['legend']['title']['size'] + """' /></td>
				</tr><tr>
					<td>Entry Size:</td>
					<td><input type='text' name='/legend/entries@height' value='""" + settings['legend']['entries']['height'] + """' /></td>
				</tr>
			</table>
		</fieldset>
	""")
	closePage(f,'settings')

def dataPage(f):
	"""Writes the data page for the GUI.
	@param f: File to write to
	"""
	openPage(f,'data')
	f.write("""
		File Format:<br />
		<input type="radio" name="data_file_type" value="csv" checked="checked" /> CSV<br />
		<input type="radio" name="data_file_type" value="xml" /> XML<br />
		<br />
		File:
		<input type="file" name="data_files" multiple="multiple" /><br />
		<br />
		Please follow the following guidelines for CSV files:
		<ul>
			<li>Each line must represent exactly one data point.</li>
			<li>The first value is the x coordinate. The second is the y coordinate.</li>
			<li>Do not include a header line.</li>
		</ul>
		Please follow the following guidelines for XML files:
		<ul>
			<li>The root element must be &lt;data&gt;.</li>
			<li>Each data set must be enclosed in a &lt;set&gt; element.</li>
			<li>Each &lt;set&gt; element should have an id attribute; the first should be set1.</li>
			<li>Each data point is represented by a &lt;value&gt; element with x and y attributes corresponding to its coordinates.</li>
		</ul>
	""")
	closePage(f,'data')

def scriptsPage(f):
	"""Writes the scripts page for the GUI.
	@param f: File to write to
	"""
	openPage(f,'scripts')
	f.write("""
		Select built-in scripts:<br />
		<input type='checkbox' name='script_tooltips' /> Tooltips<br />
		<input type='checkbox' name='script_panandzoom' /> Pan and Zoom<br />
	""")
	closePage(f,'scripts')

def submissionPage(f):
	"""Writes the submission page for the GUI.
	@param f: File to write to
	"""
	openPage(f,'submission')
	f.write("""
	Please specify output file names for the settings, data and scripts used to generate the chart.
	These will remain in the svgchart/genxml/ directory after chart generation so that you may use
	them in the future to generate this chart or modify them to produce a new chart.<br />
	WARNING: These will overwrite any files with the same names in the svgchart/genxml/ directory!
	<table>
		<tr>
			<td>Settings File:</td>
			<td><input type='text' name='outfile_settings' value='settings.xml' /></td>
		</tr><tr>
			<td>Data File:</td>
			<td><input type='text' name='outfile_data' value='data.xml' /></td>
		</tr><tr>
			<td>Scripts File:</td>
			<td><input type='text' name='outfile_scripts' value='scripts.xml' /></td>
		</tr>
	</table>
	<div style='text-align: center;'><input type="submit" value="Generate Chart" style='font-weight: bold;' /></div>
	To save the chart once it has been generated, please use your browser's Save function.
	""")
	closePage(f,'submission')

def openPage(f,label):
	"""Initializes a tabbed page section.
	@param f: File to write to
	@param label: Label for the page
	"""
	f.write("<div id='" + label + "page'>")

def closePage(f,label):
	"""Closes a tabbed page section.
	@param f: File to write to
	@param label: Label for the page
	"""
	f.write("</div>")
	openScript(f)
	f.write("pages.push(document.getElementById('" + label + "page'))")
	closeScript(f)

def closeForm(f):
	"""Closes the form for the GUI.
	@param f: File to write to
	"""
	f.write("</form>")

def footer(f):
	"""Writes the closing section of the GUI.
	@param f: File to write to
	"""
	f.write("""
</body>
</html>
	""")

def openScript(f):
	"""Opens a script section.
	@param f: File to write to
	"""
	f.write("\n<script type='text/ecmascript'>\n<!--\n")

def closeScript(f):
	"""Closes a script section.
	@param f: File to write to
	"""
	f.write("\n// -->\n</script>\n")