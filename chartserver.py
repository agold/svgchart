import urlparse
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from svgchart import getChart
from lib.gui.form import getGUI
import webbrowser

class ChartHandler(BaseHTTPRequestHandler):

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
		server = HTTPServer(('', 35782), ChartHandler)
		print 'Started chart server...'
		webbrowser.open('http://localhost:35782/',2)
		server.serve_forever()
	
	# Triggers when you type ctrl+c at the command line
	except KeyboardInterrupt:
		print 'Interrupt received, shutting down server'
		server.socket.close()

