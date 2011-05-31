import cgi
import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from svgchart import getChart
from lib.gui.form import getGUI
import webbrowser

try:
	import xml.etree.cElementTree as ETree
except:
	import xml.etree.ElementTree as ETree
import re

def addXml(root,path,value):
	"""Adds an XML node or attribute to a tree of Elements.
	@param root: The root of the tree of Elements
	@param path: The path to the node or attribute. /elem/elem, /elem@attr, /elem@style$sty, etc.
	@param value: The value to be stored at path. May be inner text, attribute value, or style value depending on path.
	"""
	if (value != ""):
		elem = root
		while path.startswith('/'):
			parts = re.split('([/@$])',path[1:],1)
			if (len(parts) > 2):
				path = parts[1] + parts[2]
			else:
				path = ""
			for child in list(elem):
				if (child.tag == parts[0]):
					break
			if (len(elem) > 0 and child.tag == parts[0]):
				elem = child
			else:
				elem = ETree.SubElement(elem,parts[0])
		if (path == ""):
			elem.text = value
		elif (path.startswith('@')):
			path = path[1:]
			if (path.startswith('style$')):
				path = path[6:]
				elem.set('style',elem.get('style',"") + path + ": " + value + ";")
			else:
				elem.set(path,value)

def csvLineToXmlValue(line):
	"""Converts a CSV line to an XML data point.
	@param line: CSV line containing x and y coordinates
	"""
	line = line.strip()
	coords = line.split(',')
	if (len(coords) >= 2):
		coords[0] = coords[0].strip("\" \t\r\n")
		coords[1] = coords[1].strip("\" \t\r\n")
		return "<value x='" + coords[0] + "' y='" + coords[1] + "' />"
	else:
		return ""

def csvToXmlData(infiles,outfile):
	"""Converts one or more CSV input files to a single XML data file.
	@param infiles: List of CSV input files
	@param outfile: File to write XML output to. Should be empty.
	"""
	outfile.write("<?xml version='1.0' encoding='UTF-8' ?>")
	outfile.write("<data>")
	i = 1
	for infile in infiles:
		outfile.write("<set id='set" + str(i) + "'>")
		i += 1
		for line in infile:
			outfile.write(csvLineToXmlValue(line))
		outfile.write("</set>")
	outfile.write("</data>")

def combineXmlData(infiles,outfile):
	"""Converts XML data input files into a single XML data file.
	@param infiles: List of XML data input files
	@param outfile: File to write XML output to. Should be empty.
	"""
	outfile.write("<?xml version='1.0' encoding='UTF-8' ?>")
	outfile.write("<data>")
	for infile in infiles:
		text = infile.read()
		match = re.search(r'<data(?: [^>]+)? *>(.*)<\/data>',text,re.DOTALL)
		if (match):
			outfile.write(match.group(1))
	outfile.write("</data>")

def builtinScripts(scriptnames,outfile):
	"""Generates XML script file for specified built-in scripts.
	@param scriptnames: List of names of built-in scripts to include.
	@param outfile: File to write XML output to. Should be empty.
	"""
	outfile.write("<?xml version='1.0' encoding='UTF-8' ?>")
	outfile.write("<scripts>")
	i = 1
	for scriptname in scriptnames:
		outfile.write("<script id='script" + str(i) + "' file='scripts/" + scriptname + ".js' />")
	outfile.write("</scripts>")

class ChartHandler(BaseHTTPRequestHandler):

	def do_POST(self):
		"""Handles a POST request, which is assumed to be from the GUI."""
		form = cgi.FieldStorage(fp=self.rfile,headers=self.headers,
								environ={'REQUEST_METHOD':'POST','CONTENT_TYPE':self.headers['Content-Type']})

		outfiles = dict()
		for key in ['outfile_settings','outfile_data','outfile_scripts']:
			outfiles[key[8:]] = "genxml/" + form.getfirst(key)

		# Settings
		sroot = ETree.Element('settings')
		for key in form:
			if (key.startswith('/')):
				for path in key.split(','):
					addXml(sroot,path,form.getfirst(key))
		stree = ETree.ElementTree(element=sroot)
		with open(outfiles['settings'],'w') as sfile:
			stree.write(sfile,encoding='utf-8',xml_declaration=True)

		# Data
		with open(outfiles['data'],'w') as dfile:
			fileitemlist = form['data_files']
			if (not isinstance(fileitemlist,list)):
				fileitemlist = [fileitemlist]
			filelist = []
			for fileitem in fileitemlist:
				filelist.append(fileitem.file)
			if (form.getfirst('data_file_type') == 'csv'):
				csvToXmlData(filelist,dfile)
			elif (form.getfirst('data_file_type') == 'xml'):
				combineXmlData(filelist,dfile)

		# Scripts
		with open(outfiles['scripts'],'w') as cfile:
			scriptnames = []
			for key in form:
				if (key.startswith('script_')):
					scriptnames.append(key[7:])
			builtinScripts(scriptnames,cfile)

		try:
			self.send_response(200)
			self.send_header('Content-type','image/svg+xml')
			self.end_headers()
			getChart(None, outfiles['settings'], outfiles['data'], outfiles['scripts'], self.wfile, form.getfirst('type'), False, ',,,')
		except:
			self.wfile.write("""<?xml version='1.0' encoding='utf-8'?>
			<svg verson='1.1' xmlns='http://www.w3.org/2000/svg'>
				<text x='10' y='25'>An error occured during chart generation. Please use your browser's Back
				button to return to the previous page and make sure that all input is valid.</text>
			</svg>
			""")

	def do_GET(self):
		
		# Parse the query out of the path
		query = urlparse.urlparse(self.path).query
		form = urlparse.parse_qs(query)
		
		# Make sure at least some input is specified
		if "infile" not in form and "settings" not in form and "data" not in form:
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()

			getGUI(self.wfile)
			return
		else:
			if "infile" in form:
				infile = form["infile"][0]
			else:
				infile = None
			
			if "settings" in form:
				settings = form["settings"][0]
			else:
				settings = None
			
			if "data" in form:
				data = form["data"][0]
			else:
				data = None
				
			if "scripts" in form:
				scripts = form["scripts"][0]
			else:
				scripts = None
			
			if "type" in form:
				type = form["type"][0]
			else:
				type = 'scatter'
			
			if "range" in form:
				range = form["range"][0]
			else:
				range = ',,,'
			
			pretty = "pretty" in form
			
			# Send success headers and the SVG MIME type
			self.send_response(200)
			self.send_header('Content-type', 'image/svg+xml')
			self.end_headers()
			
			# Gets the chart and writes directly to the client
			getChart(infile, settings, data, scripts, self.wfile, type, pretty, range)
			
if __name__ == '__main__':
	try:
		# Start listening on some port. It doesn't matter which one
		server = HTTPServer(('', 35785), ChartHandler)
		print 'Started chart server...'
		webbrowser.open('http://localhost:35785/',2)
		server.serve_forever()
	
	# Triggers when you type ctrl+c at the command line
	except KeyboardInterrupt:
		print 'Interrupt received, shutting down server'
		server.socket.close()

