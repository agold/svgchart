def getGUI(f):
	header(f)
	initColors(f,['red','green','blue'])
	initTabs(f,['settings','data','scripts'])
	openPage(f,'settings')
	f.write("Some settings")
	closePage(f,'settings')
	openPage(f,'data')
	f.write("Some data")
	closePage(f,'data')
	openPage(f,'scripts')
	f.write("Some scripts")
	closePage(f,'scripts')
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
		var colors = new Array()
		var tabs = new Array()
		var pages = new Array()
		function init_tabs() {
			for (var i = 0;i < pages.length;i++)
				pages[i].setAttribute('class',colors[i] + ' page')
			select_tab(tabs[0])
		}
		function reset_tabs() {
			for (var i = 0;i < tabs.length;i++) {
				tabs[i].setAttribute('class',colors[i] + ' tab')
				pages[i].style.display = 'none'
			}
		}
		function select_tab(tab) {
			reset_tabs()
			page = pages[tabs.indexOf(tab)]
			tab.setAttribute('class',tab.getAttribute('class') + ' selected')
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
	height: 20px;
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
	height: 70%;
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

def openPage(f,label):
	f.write("<div id='" + label + "page'>")

def closePage(f,label):
	f.write("</div>")
	openScript(f)
	f.write("pages.push(document.getElementById('" + label + "page'))")
	closeScript(f)

def footer(f):
	f.write("""
</body>
</html>
	""")

def openScript(f):
	f.write("\n<script type='text/javascript'>\n<!--\n")

def closeScript(f):
	f.write("\n// -->\n</script>\n")