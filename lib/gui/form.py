def getGUI(f):
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
	f.write("""
		<html>
		<head>
			<title>GUI</title>
	""")
	style(f)
	tabScript(f)
	f.write("""
		</head>
		<body onload='init_tabs()'>
	""")

def style(f):
	f.write("<style type='text/css'>")
	with open('lib/gui/style.css','r') as stylesheet:
		f.write(stylesheet.read())
	f.write("</style>")

def tabScript(f):
	f.write("""<script type='text/javascript'>
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
	</script>
	""")

def initColors(f,colors):
	openScript(f)
	for color in colors:
		f.write("colors.push('" + color + "')\n")
	closeScript(f)

def initTabs(f,labels):
	for label in labels:
		f.write("<div id='" + label + "tab' onclick='select_tab(this)'>" + label.capitalize() + "</div>")
		openScript(f)
		f.write("tabs.push(document.getElementById('" + label + "tab'))")
		closeScript(f)

def openForm(f):
	f.write("<form enctype='multipart/form-data' action='.' method='post' style='display:inline;'>")

def settingsPage(f):
	openPage(f,'settings')
	f.write("""
		<fieldset><legend>Type</legend>
			<input type='radio' name='type' value='scatter' checked='checked' /> Scatter
			<input type='radio' name='type' value='line' /> Line
		</fieldset>
		<fieldset><legend>Chart Area</legend>
			<table>
				<tr>
					<td>Size:</td>
					<td><input type='text' name='/chart@width' value='650' /> x <input type='text' name='/chart@height' value='400' /></td>
				</tr><tr>
					<td>Background:</td>
					<td><input type='text' name='/chart/border@style$fill' value='none' /></td>
				</tr><tr>
					<td>Border Color:</td>
					<td><input type='text' name='/chart/border@style$stroke' value='black' /></td>
				</tr><tr>
					<td>Border Width:</td>
					<td><input type='text' name='/chart/border@style$stroke-width' value='1px' /></td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Title</legend>
			<table>
				<tr>
					<td>Title:</td>
					<td><input type='text' name='/title/title' value='The title' /></td>
				</tr><tr>
					<td>Subtitle:</td>
					<td><input type='text' name='/title/subtitle' /></td>
				</tr><tr>
					<td>Size:</td>
					<td><input type='text' name='/title@width' /> x <input type='text' name='/title@height' /></td>
				</tr><tr>
					<td>Location:</td>
					<td><input type='text' name='/title@x' /> , <input type='text' name='/title@y' /> (top left corner coordinates)</td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>X-Axis</legend>
			<table>
				<tr>
					<td>Major Tick Number:</td>
					<td><input type='text' name='/x-axis/majors@count' /></td>
				</tr><tr>
					<td>Major Tick Size:</td>
					<td><input type='text' name='/x-axis/majors@size' /></td>
				</tr><tr>
					<td>Minor Tick Number:</td>
					<td><input type='text' name='/x-axis/minors@count' /></td>
				</tr><tr>
					<td>Minor Tick Size:</td>
					<td><input type='text' name='/x-axis/minors@size' /></td>
				</tr><tr>
					<td>Label Format:</td>
					<td><input type='text' name='/x-axis/labels@format' /> (e.g. %d for integer, %.2f for 2 decimal places)</td>
				</tr><tr>
					<td>Range Min:</td>
					<td><input type='text' name='/x-axis/range@min' value='auto' /></td>
				</tr><tr>
					<td>Range Max:</td>
					<td><input type='text' name='/x-axis/range@max' value='auto' /></td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Y-Axis</legend>
			<table>
				<tr>
					<td>Major Tick Number:</td>
					<td><input type='text' name='/y-axis/majors@count' /></td>
				</tr><tr>
					<td>Major Tick Size:</td>
					<td><input type='text' name='/y-axis/majors@size' /></td>
				</tr><tr>
					<td>Minor Tick Number:</td>
					<td><input type='text' name='/y-axis/minors@count' /></td>
				</tr><tr>
					<td>Minor Tick Size:</td>
					<td><input type='text' name='/y-axis/minors@size' /></td>
				</tr><tr>
					<td>Label Format:</td>
					<td><input type='text' name='/y-axis/labels@format' /> (e.g. %d for integer, %.2f for 2 decimal places)</td>
				</tr><tr>
					<td>Range Min:</td>
					<td><input type='text' name='/y-axis/range@min' value='auto' /></td>
				</tr><tr>
					<td>Range Max:</td>
					<td><input type='text' name='/y-axis/range@max' value='auto' /></td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Data Area</legend>
			<table>
				<tr>
					<td>Size:</td>
					<td><input type='text' name='/datafield@width' /> x <input type='text' name='/datafield@height' /></td>
				</tr><tr>
					<td>Location:</td>
					<td><input type='text' name='/datafield@x' /> , <input type='text' name='/datafield@y' /> (top left corner coordinates)</td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Dataset</legend>
			<table>
				<tr>
					<td>Symbol:</td>
					<td>Shape:</td>
					<td><input type='text' name='/datasets/set/symbol@shape' /></td>
				</tr><tr>
					<td></td>
					<td>Size:</td>
					<td><input type='text' name='/datasets/set/symbol@size' /></td>
				</tr><tr>
					<td></td>
					<td>Color:</td>
					<td><input type='text' name='/datasets/set/symbol@style$fill' /></td>
				</tr><tr>
					<td>Line:</td>
					<td>Color:</td>
					<td><input type='text' name='/datasets/set/line@style$stroke' /></td>
				</tr><tr>
					<td></td>
					<td>Width:</td>
					<td><input type='text' name='/datasets/set/line@style$stroke-width' /> (pixels--please end with "px", e.g. 1px)</td>
				</tr>
			</table>
		</fieldset>
		<fieldset><legend>Legend</legend>
			<table>
				<tr>
					<td>Size:</td>
					<td><input type='text' name='/legend@width' /> x <input type='text' name='/legend@height' /></td>
				</tr><tr>
					<td>Location:</td>
					<td><input type='text' name='/legend@x' /> , <input type='text' name='/legend@y' /> (top left corner coordinates)</td>
				</tr><tr>
					<td>Title:</td>
					<td><input type='text' name='/legend/title' /></td>
				</tr><tr>
					<td>Title Size:</td>
					<td><input type='text' name='/legend/title@size' /></td>
				</tr><tr>
					<td>Entry Size:</td>
					<td><input type='text' name='/legend/entries@height' /></td>
				</tr>
			</table>
		</fieldset>
	""")
	closePage(f,'settings')

def dataPage(f):
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
	openPage(f,'scripts')
	f.write("""
		Select built-in scripts:<br />
		<input type='checkbox' name='script_tooltips' /> Tooltips<br />
		<input type='checkbox' name='script_panandzoom' /> Pan and Zoom<br />
	""")
	closePage(f,'scripts')

def submissionPage(f):
	openPage(f,'submission')
	f.write("""
	<div style='text-align: center;'><input type="submit" value="Generate Chart" style='font-weight: bold;' /></div>
	""")
	closePage(f,'submission')

def openPage(f,label):
	f.write("<div id='" + label + "page'>")

def closePage(f,label):
	f.write("</div>")
	openScript(f)
	f.write("pages.push(document.getElementById('" + label + "page'))")
	closeScript(f)

def closeForm(f):
	f.write("</form>")

def footer(f):
	f.write("""
</body>
</html>
	""")

def openScript(f):
	f.write("\n<script type='text/javascript'>\n<!--\n")

def closeScript(f):
	f.write("\n// -->\n</script>\n")