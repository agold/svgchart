if (typeof panandzoom == 'undefined') {
	panandzoom = {
		svgns: "http://www.w3.org/2000/svg",
		querystring: "%%querystring%%",
		requestPage: "/",
		bounds: {"x": {"min": %%data[x][min][real]%%, "max": %%data[x][max][real]%%}, "y": {"min": %%data[y][min][real]%%, "max": %%data[y][max][real]%%}},
		values: {"x": {"min": %%data[x][min][current]%%, "max": %%data[x][max][current]%%}, "y": {"min": %%data[y][min][current]%%, "max": %%data[y][max][current]%%}},
		coords: {"x": {"begin": %%settings[datafield][x]%%, "end": %%settings[datafield][x]%% + %%settings[datafield][width]%%},
			   "y": {"begin": %%settings[datafield][y]%% + %%settings[datafield][height]%%, "end": %%settings[datafield][y]%%}},
		ids: {"datafield": "%%settings[datafield][id]%%", "xaxis": "%%settings[x-axis][id]%%", "yaxis": "%%settings[y-axis][id]%%"},
		controls: {},
		init: function() {
			panandzoom.drawXAxisControls();
			panandzoom.drawYAxisControls();

		},
		createControl: function(x, y, r, direction, labeltext) {
			var controlGroup = document.createElementNS(panandzoom.svgns, "g");
			var label = document.createElementNS(panandzoom.svgns, "text");
			label.appendChild(document.createTextNode(labeltext));

			var control = document.createElementNS(panandzoom.svgns, "path");
			if (direction == "x") {
				var cursor = "w-resize";
				control.addEventListener("mousedown", panandzoom.grabControlX, false);
				label.setAttributeNS(null, "x", 5);
				label.setAttributeNS(null, "y", 14);
				label.setAttributeNS(null, "style", "text-anchor: middle;");
			}
			else {
				var cursor = "n-resize";
				control.addEventListener("mousedown", panandzoom.grabControlY, false);
				label.setAttributeNS(null, "x", -1);
				label.setAttributeNS(null, "y", 11);
				label.setAttributeNS(null, "style", "text-anchor: end;");
			}
			control.setAttributeNS(null, "d", "M 0,0 L 0,10 L 5,10 L 10,5 L 5,0 L 0,0 Z");
			control.setAttributeNS(null, "style", "stroke: black; stroke-width: 2px; fill: white; cursor: " + cursor + ";");
			control.setAttributeNS(null, "transform", "rotate(" + r + ")");
			//control.setAttributeNS(null, "xpos", x + 5);
			//control.setAttributeNS(null, "ypos", y + 5);

			controlGroup.appendChild(control);
			controlGroup.appendChild(label);
			controlGroup.setAttributeNS(null, "transform", "translate(" + x +", " + y + ")");
			controlGroup.setAttributeNS(null, "xpos", x + 5);
			controlGroup.setAttributeNS(null, "ypos", y + 5);

			return controlGroup;
		},
		drawXAxisControls: function() {
			var left = document.createElementNS(panandzoom.svgns, "line");
			left.setAttributeNS(null, "x1", panandzoom.coords.x.begin);
			left.setAttributeNS(null, "x2", panandzoom.coords.x.begin);
			left.setAttributeNS(null, "y1", panandzoom.coords.y.begin + 20);
			left.setAttributeNS(null, "y2", panandzoom.coords.y.begin + 30);
			left.setAttributeNS(null, "style", "stroke: black; stroke-width: 1px;");
			var right = document.createElementNS(panandzoom.svgns, "line");
			right.setAttributeNS(null, "x1", panandzoom.coords.x.end);
			right.setAttributeNS(null, "x2", panandzoom.coords.x.end);
			right.setAttributeNS(null, "y1", panandzoom.coords.y.begin + 20);
			right.setAttributeNS(null, "y2", panandzoom.coords.y.begin + 30);
			right.setAttributeNS(null, "style", "stroke: black; stroke-width: 1px;");
			var track = document.createElementNS(panandzoom.svgns, "line");
			track.setAttributeNS(null, "x1", panandzoom.coords.x.begin);
			track.setAttributeNS(null, "x2", panandzoom.coords.x.end);
			track.setAttributeNS(null, "y1", panandzoom.coords.y.begin + 25);
			track.setAttributeNS(null, "y2", panandzoom.coords.y.begin + 25);
			track.setAttributeNS(null, "style", "stroke: black; stroke-width: 1px;");

			var leftControl = panandzoom.createControl(panandzoom.coords.x.begin - 5, panandzoom.coords.y.begin + 35, 270, "x", panandzoom.values.x.min);
			var rightControl = panandzoom.createControl(panandzoom.coords.x.end - 5, panandzoom.coords.y.begin + 35, 270, "x", panandzoom.values.x.max);


			var xaxis = document.createElementNS(panandzoom.svgns, "g");
			xaxis.appendChild(left);
			xaxis.appendChild(right);
			xaxis.appendChild(track);
			xaxis.appendChild(leftControl);
			xaxis.appendChild(rightControl);

			document.rootElement.appendChild(xaxis);

			panandzoom.controls.x = {"left": leftControl, "right": rightControl};
		},
		drawYAxisControls: function() {
			var bottom = document.createElementNS(panandzoom.svgns, "line");
			bottom.setAttributeNS(null, "x1", panandzoom.coords.x.begin - 25);
			bottom.setAttributeNS(null, "x2", panandzoom.coords.x.begin - 35);
			bottom.setAttributeNS(null, "y1", panandzoom.coords.y.begin);
			bottom.setAttributeNS(null, "y2", panandzoom.coords.y.begin);
			bottom.setAttributeNS(null, "style", "stroke: black; stroke-width: 1px;");
			var top = document.createElementNS(panandzoom.svgns, "line");
			top.setAttributeNS(null, "x1", panandzoom.coords.x.begin - 25);
			top.setAttributeNS(null, "x2", panandzoom.coords.x.begin - 35);
			top.setAttributeNS(null, "y1", panandzoom.coords.y.end);
			top.setAttributeNS(null, "y2", panandzoom.coords.y.end);
			top.setAttributeNS(null, "style", "stroke: black; stroke-width: 1px;");
			var track = document.createElementNS(panandzoom.svgns, "line");
			track.setAttributeNS(null, "x1", panandzoom.coords.x.begin - 30);
			track.setAttributeNS(null, "x2", panandzoom.coords.x.begin - 30);
			track.setAttributeNS(null, "y1", panandzoom.coords.y.begin);
			track.setAttributeNS(null, "y2", panandzoom.coords.y.end);
			track.setAttributeNS(null, "style", "stroke: black; stroke-width: 1px;");
			var bottomControl = panandzoom.createControl(panandzoom.coords.x.begin - 40, panandzoom.coords.y.begin - 5, 0, "y", panandzoom.values.y.min);
			var topControl = panandzoom.createControl(panandzoom.coords.x.begin - 40, panandzoom.coords.y.end - 5, 0, "y", panandzoom.values.y.max);

			var yaxis = document.createElementNS(panandzoom.svgns, "g");
			yaxis.appendChild(bottom);
			yaxis.appendChild(top);
			yaxis.appendChild(track);
			yaxis.appendChild(bottomControl);
			yaxis.appendChild(topControl);

			document.rootElement.appendChild(yaxis);

			panandzoom.controls.y = {"top": topControl, "bottom": bottomControl};
		},
		grabControlX: function(evt) {
			panandzoom.activeControl = evt.target.parentNode;
			document.rootElement.setAttributeNS(null, "pointer-events", "none");
			document.addEventListener("mousemove", panandzoom.dragControlX, false);
			document.addEventListener("mouseup", panandzoom.dropControlX, false);
		},
		dragControlX: function(evt) {
			var x = evt.clientX;
			var bbox = panandzoom.activeControl.getBBox();
			var newx = x - bbox.width / 2;
			if ((x - 4) >= panandzoom.coords.x.begin && (x - 4) <= panandzoom.coords.x.end) {
				var oldtransform = panandzoom.activeControl.getAttributeNS(null, 'transform');
				var newtransform = oldtransform.replace(/translate\(\s*[\d\.]+\s*,\s*([\d\.]+)\s*\)/, "translate(" + newx + ", $1)");
				panandzoom.activeControl.setAttributeNS(null, "transform", newtransform);
				panandzoom.activeControl.setAttributeNS(null, "xpos", x);
				var label = panandzoom.activeControl.lastChild;
				label.removeChild(label.firstChild);
				label.appendChild(document.createTextNode(Math.round(panandzoom.XCoordToValue(x))));
			}
		},
		dropControlX: function(evt) {
			panandzoom.activeControl = null;
			document.rootElement.setAttributeNS(null, "pointer-events", "all");
			document.removeEventListener("mousemove", panandzoom.dragControlX, false);
			document.removeEventListener("mouseup", panandzoom.dropControlX, false);

			panandzoom.updateRanges();
		},
		grabControlY: function(evt) {
			panandzoom.activeControl = evt.target.parentNode;
			document.rootElement.setAttributeNS(null, "pointer-events", "none");
			document.addEventListener("mousemove", panandzoom.dragControlY, false);
			document.addEventListener("mouseup", panandzoom.dropControlY, false);
		},
		dragControlY: function(evt) {
			var y = evt.clientY;
			var bbox = panandzoom.activeControl.getBBox();
			var newy = y - bbox.height / 2;
			if ((y - 4) <= panandzoom.coords.y.begin && (y - 4) >= panandzoom.coords.y.end) {
				var oldtransform = panandzoom.activeControl.getAttributeNS(null, 'transform');
				var newtransform = oldtransform.replace(/translate\(\s*([\d\.]+)\s*,\s*[\d\.]+\s*\)/, "translate($1, " + newy + ")");
				panandzoom.activeControl.setAttributeNS(null, "transform", newtransform);
				panandzoom.activeControl.setAttributeNS(null, "ypos", y);
				var label = panandzoom.activeControl.lastChild;
				label.removeChild(label.firstChild);
				label.appendChild(document.createTextNode(Math.round(panandzoom.YCoordToValue(y))));
			}
		},
		dropControlY: function(evt) {
			panandzoom.activeControl = null;
			document.rootElement.setAttributeNS(null, "pointer-events", "all");
			document.removeEventListener("mousemove", panandzoom.dragControlY, false);
			document.removeEventListener("mouseup", panandzoom.dropControlY, false);

			panandzoom.updateRanges();
		},
		updateRanges: function() {
			var left = panandzoom.controls.x.left.getAttributeNS(null, "xpos");
			var right = panandzoom.controls.x.right.getAttributeNS(null, "xpos");
			var top = panandzoom.controls.y.top.getAttributeNS(null, "ypos");
			var bottom = panandzoom.controls.y.bottom.getAttributeNS(null, "ypos");

			var xmin = panandzoom.XCoordToValue(left);
			var xmax = panandzoom.XCoordToValue(right);
			var ymin = panandzoom.YCoordToValue(bottom);
			var ymax = panandzoom.YCoordToValue(top);
			var range = "&range=" + xmin + "," + xmax + "," + ymin + "," + ymax;

			http = new XMLHttpRequest();

			http.open("GET", panandzoom.requestPage + panandzoom.querystring + range, true);
			http.onreadystatechange = function() {
				panandzoom.handleResponse(http);
			}
			http.send(null)
		},
		handleResponse: function(http) {
			if (http.readyState == 4) {
				var newxml = http.responseXML;
				var datafield = document.importNode(newxml.getElementById(panandzoom.ids.datafield), true);
				var xaxis = document.importNode(newxml.getElementById(panandzoom.ids.xaxis), true);
				var yaxis = document.importNode(newxml.getElementById(panandzoom.ids.yaxis), true);
				document.rootElement.replaceChild(datafield, document.getElementById(panandzoom.ids.datafield));
				document.rootElement.replaceChild(xaxis, document.getElementById(panandzoom.ids.xaxis));
				document.rootElement.replaceChild(yaxis, document.getElementById(panandzoom.ids.yaxis));
			}
		},
		XCoordToValue: function(coord) {
			return (coord * panandzoom.values.x.max - coord * panandzoom.values.x.min - panandzoom.coords.x.begin * panandzoom.values.x.max + panandzoom.coords.x.end * panandzoom.values.x.min) / (panandzoom.coords.x.end - panandzoom.coords.x.begin);
		},
		YCoordToValue: function(coord) {
			return (coord * panandzoom.values.y.max - coord * panandzoom.values.y.min - panandzoom.coords.y.begin * panandzoom.values.y.max + panandzoom.coords.y.end * panandzoom.values.y.min) / (panandzoom.coords.y.end - panandzoom.coords.y.begin);
		}
	};
	window.addEventListener("load", panandzoom.init, false);
}
