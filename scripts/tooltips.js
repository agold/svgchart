if (typeof tooltips == "undefined") {
	tooltips = {
		svgns: "http://www.w3.org/2000/svg",
		ids: {"container": "tooltip-container", "rect": "tooltip-rect", "contents": "tooltip-contents", "overlay": "tooltip-datafield-overlay"},
		elems: {},
		field : {"x": %%settings[datafield][x]%%, "y": %%settings[datafield][y]%%, "width": %%settings[datafield][width]%%, "height": %%settings[datafield][height]%%},
		datasets: %%datasets%%,
		init: function(evt) {
			tooltips.points = null;
			tooltips.activePoints = null;
			tooltips.convertPoints();
			tooltips.makeToolTip();
			tooltips.overlay();
		},
		makeToolTip: function() {
			var container = document.createElementNS(tooltips.svgns, "g");
			container.setAttributeNS(null, "id", tooltips.ids.container);

			var rect = document.createElementNS(tooltips.svgns, "rect");
			rect.setAttributeNS(null, "id", tooltips.ids.rect);
			rect.setAttributeNS(null, "rx", 4);
			rect.setAttributeNS(null, "ry", 4);
			rect.setAttributeNS(null, "style", "fill:#FFFFFF; fill-opacity:0.7; stroke: #000000; stroke-opacity:0.7;stroke-width: 2px;");

			var contents = document.createElementNS(tooltips.svgns, "g");
			contents.setAttributeNS(null, "id", tooltips.ids.contents);

			container.appendChild(rect);
			container.appendChild(contents);
			document.rootElement.appendChild(container);

			tooltips.elems.container = container;
			tooltips.elems.rect = rect;
			tooltips.elems.contents = contents;
		},
		overlay: function() {
			var overlay = document.createElementNS(tooltips.svgns, "rect");
			overlay.setAttributeNS(null, "id", tooltips.ids.overlay);
			overlay.setAttributeNS(null, "x", tooltips.field.x);
			overlay.setAttributeNS(null, "y", tooltips.field.y);
			overlay.setAttributeNS(null, "width", tooltips.field.width);
			overlay.setAttributeNS(null, "height", tooltips.field.height);
			overlay.setAttributeNS(null, "opacity", 0);
			
			overlay.addEventListener('mousemove', tooltips.dataOver, false);
			overlay.addEventListener('mouseout', tooltips.dataOut, false);
			
			document.rootElement.appendChild(overlay);

			tooltips.elems.overlay = overlay;		
		},
		convertPoints: function() {
			var result = [];
			for (setid in tooltips.datasets) {
				var l = tooltips.datasets[setid].values.length;
				var setcolor = null;
				for (var i = 0; i < l; i++) {
					if (setcolor == null) {
						var point = document.getElementById(tooltips.datasets[setid].values[i].id);
						if (point.currentStyle)
							setcolor = x.currentStyle["fill"];
						else if (window.getComputedStyle)
							setcolor = document.defaultView.getComputedStyle(point, null).getPropertyValue("fill");
						else setcolor = "#000000";
					}
					x = tooltips.datasets[setid].values[i].coord.x;
					var floored = Math.floor(x);
					if (typeof result[floored] == 'undefined') {
						result[floored] = [];
					}
					var newpoint = tooltips.datasets[setid].values[i];
					newpoint.setid = setid;
					newpoint.color = setcolor;
					result[floored].push(newpoint);
				}
			}
			var end = tooltips.field.x + tooltips.field.width;
			for (var i = tooltips.field.x; i <= end; i++) {
				if (typeof result[i] == 'undefined') {
					result[i] = {};
					var prev = 0;
					var next = end + 1;
					for (j = tooltips.field.x; j <= end; j++) {
						if (typeof result[j] != 'undefined') {
							if (j < i && j > prev) prev = j;
							else if (j > i && j < next) next = j;
						}
					}
					if ((i - prev) > (next - i)) result[i] = result[next];
					else result[i] = result[prev];
				}
			}
			tooltips.points = result;
		},
		dataOver: function(evt) {
			var posx = 0;
			if (evt.pageX) {
				posx = evt.pageX
			} else if (evt.clientX) {
				// I don't imagine this will ever work. An XML document doesn't have a "body"
				posx = evt.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
			}

			var points = tooltips.points[posx];
			
			if (points != tooltips.activePoints) {
				if (tooltips.activePoints) {
					for (i = 0; i < tooltips.activePoints.length; i++) {
						tooltips.deactivatePoint(tooltips.activePoints[i]);
					}
				}
				var firstPoint = null;
				for (i = 0; i < points.length; i++) {
					if (firstPoint == null && document.getElementById(points[i].id).parentNode.getAttribute('visibility') != 'hidden') {
						firstPoint = points[i];
					}
					tooltips.activatePoint(points[i]);
				}
				var x = firstPoint.coord.x
				var y = firstPoint.coord.y

				tooltips.showToolTip(x, y, tooltips.ttNode(posx), tooltips.field.width + tooltips.field.x);
				tooltips.activePoints = points;
			}
		},
		dataOut: function(evt) {

			if (tooltips.activePoints != null) {
				for (var i = 0; i < tooltips.activePoints.length; i++) {
					tooltips.deactivatePoint(tooltips.activePoints[i]);
				}
				tooltips.hideToolTip();
				tooltips.activePoints = null;
			}
		},
		activatePoint: function(point) {
			var elem = document.getElementById(point.id);
			if (elem) {
				var translate1 = "translate(" + point.coord.x + ", " + point.coord.y + ")";
				var translate2 = "translate(-" + point.coord.x + ", -" + point.coord.y + ")";
				elem.setAttributeNS(null, 'transform', translate1 + ' scale(1.5, 1.5) ' + translate2)
			}
		},
		deactivatePoint: function(point) {
			var elem = document.getElementById(point.id);
			if (elem) {
				elem.removeAttributeNS(null, 'transform')
			}
		},
		ttNode: function(xpos) {
			var points = tooltips.points[xpos];

			var container = document.createElementNS(tooltips.svgns, 'text');
			container.setAttributeNS(null, 'class', 'tooltip-text');
			container.setAttributeNS(null, 'y', 0);
			container.setAttributeNS(null, 'x', 2);

			var currentY = 0;
			for (i = 0; i < points.length; i++) {
				var point = points[i];
				var dataset = point.setid;
				var dataid = point.id;
				var color = point.color;
				var setName = tooltips.datasets[point.setid].label; //tooltips should be the set name as given in the legend instead
				var yvalue = point.val.y;

				if (document.getElementById(setid).getAttribute('visibility') != 'hidden') {
					if (i == 0) {
						currentY = currentY + 15;
						var xelem = document.createElementNS(tooltips.svgns, 'tspan');
						xelem.setAttributeNS(null, 'x', 2);
						xelem.setAttributeNS(null, 'y', currentY);
						xelem.appendChild(document.createTextNode("X: " + point.val.x));
						container.appendChild(xelem);
					}
					currentY = currentY + ((i == 0) ? 20 : 15);
					var setelem = document.createElementNS(tooltips.svgns, 'tspan');
					setelem.setAttributeNS(null, 'x', 2);
					setelem.setAttributeNS(null, 'y', currentY);

					var settitle = document.createElementNS(tooltips.svgns, 'tspan');
					settitle.setAttributeNS(null, 'style', 'font-weight: bold; fill: ' + color + ';');
					settitle.appendChild(document.createTextNode(setName + ': '));
					setelem.appendChild(settitle);

					var setdata = document.createElementNS(tooltips.svgns, 'tspan');
					var datastring = yvalue;
					setdata.appendChild(document.createTextNode(datastring));
					setelem.appendChild(setdata);

					container.appendChild(setelem);
				}
			}
			return container;
		},
		showToolTip: function(x, y, node, max_x) {
			var x = parseInt(x);
			var y = parseInt(y);
			var max_x = parseInt(max_x);
			var ttcontainer 	= tooltips.elems.container;
			var ttrect 			= tooltips.elems.rect;
			var ttcontents		= tooltips.elems.contents;

			tooltips.clearNode(ttcontents);
			ttcontents.appendChild(node);

			var bbox = ttcontents.getBBox();
			var ttwidth = bbox.width + 6;
			var ttheight = bbox.height + 2;
			var ttypos = y - (ttheight / 2);
			var ttxpos = x + 10;
			if (max_x) {
				var tipxbound = ttxpos + ttwidth;
				if (tipxbound >= max_x) {
					var ttxpos = x - 10 - ttwidth;
				}
			}

			ttrect.setAttributeNS(null, "width", ttwidth);
			ttrect.setAttributeNS(null, "height", ttheight);
			ttcontainer.setAttributeNS(null, "transform", "translate(" + ttxpos + "," + ttypos + ")");
			ttcontainer.setAttributeNS(null, "visibility", "visible");
		},
		hideToolTip: function() {
			var ttelem = tooltips.elems.container;
			ttelem.setAttributeNS(null, "visibility", "hidden");
		},
		clearNode: function(node) {
			while (node.childNodes.length >= 1) {
				node.removeChild(node.firstChild);
			}
		}
	};
	window.addEventListener("load", tooltips.init, false);
}
