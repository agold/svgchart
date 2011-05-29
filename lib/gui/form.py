from lib.input.InputSet import InputSet
from lib.input.FileInput import FileInput
import lib.parse.ParsedInput as ParsedInput
from lib.parse.IndexedDict import IndexedDict

def getGUI(f):
	header(f)
	initColors(f,['red','green','blue'])
	initTabs(f,['settings','data','scripts'])
	openForm(f)

	settingsPage(f)
	dataPage(f)

	openPage(f,'scripts')
	f.write("Some scripts")
	closePage(f,'scripts')

	closeForm(f)
	footer(f)

def header(f):
	f.write("""
<html>
<head>
	<title>GUI</title>
	""")
	style(f)
#	<link rel='stylesheet' type='text/css' href='lib/gui/style.css' />
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
</head>
<body onload='init_tabs()'>
	""")

def style(f):
	f.write("""<style type='text/css'>
body {
	font-family: Arial;
}

.tab {
	width: 200px;
	height: 22px;
	display: inline-block;

	text-align: center;

	border: 1px solid #111188;
	border-bottom: 0px;
	border-top-left-radius: 7px;
	border-top-right-radius: 7px;

	cursor: pointer;
}

.selected {
	font-weight: bold;
}

.page {
	border: 1px solid #111188;
	border-top-right-radius: 7px;
	border-bottom-left-radius: 7px;
	border-bottom-right-radius: 7px;
	padding: 5px;
	background-color: #EEEEFF;
}

.red {
	background-color: #FFEEEE;
	border-color: #881111;
}

.green {
	background-color: #EEFFEE;
	border-color: #118811;
}

.blue {
	background-color: #EEEEFF;
	border-color: #111188;
}
</style>""")

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
	f.write("<form enctype='multipart/form-data' action='.' method='post' style='display:inline;'><input type='submit' value='Submit' />")

def settingsPage(f):
	openPage(f,'settings')

	# Parse default file for basic structure
	defFile = "defaults/default.line.settings.xml"
	defText = InputSet('settings')
	FileInput([defText],defFile)
	defSettings = ParsedInput.parseXml(defText.textlist[0])

	inputTree(f,defSettings)

	closePage(f,'settings')

def inputTree(f,input,tag = "",path = ""):
	f.write(tag.capitalize() + ": ")
	if (isinstance(input[key],IndexedDict)):
		f.write("<input type='text' name='" + path + "/" + tag + "' value='" + str(input.text) + "' />")
		f.write("<ul>")
		for key in input.keys():
			if (key not in ["id","class"]):
				f.write("<li>")
				inputTree(f,input[key],key,path + "/" + tag)
			f.write("</li>")
		f.write("</ul>")
	else:
		f.write("<input type='text' name='" + path + "@" + tag + "' value='" + input + "' />")

def dataPage(f):
	openPage(f,'data')
	f.write("<input type='file' name='files' />")
	closePage(f,'data')

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