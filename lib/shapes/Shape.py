import lib.ElementTreeCDATA as etree

from Coordinate import Coordinate


class Shape(object):
	"""Base class of a generic shape.

	>>> shape = Shape(tag='foo', id='id', classes='class', text='bar', attrs={'spoons': 'forks'}, knives='sharp')
	>>> shape.tag
	'foo'
	>>> shape.text
	'bar'
	>>> shape.attrs
	{'spoons': 'forks', 'knives': 'sharp'}
	>>> print shape
	<foo class="class" id="id" knives="sharp" spoons="forks">bar</foo>

	"""

	def __init__(self, tag=u'', id=None, classes=None, text=None, cdata=None, subelements=None, precision=4, attrs={}, **kwargs):
		"""
		@param tag: the SVG tag name
		@type tag: string
		@param id: The unique ID to be used in the SVG document
		@type id: string
		@param classes: Classnames to be used in the SVG document
		@type classes: string or sequence of strings
		@param text: inner text of the SVG element
		@type text: string
		@param cdata: Inner text of the SVG element that will be rendered in a CDATA section
		@type cdata: string
		@param subelements: a list of subelements of this shape
		@param precision: the decimal precision for numbers in SVG output
		@type precision: integer
		@param attrs: dictionary of key-value pairs for the SVG element's attributes
		@type attrs: dict
		"""

		self.tag = tag
		self.text = text
		self.cdata = cdata
		self.subelements = subelements
		self.precision = precision
		self.attrs = dict(attrs, **kwargs)
		self.id = id
		self.classes = classes

	def __str__(self):
		"""Returns the SVG representation as a string."""

		return etree.tostring(self.svg(), 'utf-8')

	def fitToWidth(self, width=0.0):
		"""Dummy method to fit to a given width."""

		pass

	def fitToHeight(self, height=0.0):
		"""Dummy method to fit to a given height."""

		pass

	def fit(self, width=0.0, height=0.0):
		"""Fits shape to given width and height maintaining scale.

		@param width: the width to fit to
		@param height: the height to fit to
		"""

		if width <= 0 and height <= 0:
			raise ValueError("width or height must be greater than 0")

		if height < width and height > 0 or width <= 0:
			self.fitToHeight(height)
		else:
			self.fitToWidth(width)

	def translateTo(self, coord=Coordinate()):
		"""Dummy method to translate to a given coordinate."""

		pass

	def translate(self, x=0.0, y=0.0):
		"""Dummy method to translate by a given amount."""
		
		pass
	
	def svg(self):
		"""Returns the SVG representation as an XML fragment."""

		if isinstance(self.classes, basestring):
			classes = (self.classes,)
		else:
			classes = self.classes

		svgattrs = {}
		if self.id is not None:
			svgattrs["id"] = self.id
		if classes is not None:
			svgattrs["class"] = u' '.join(classes)
			
		for key in self.attrs.keys():
			try:
				# Attemt to format as float with given precision
				svgattrs[key] = u'{val:.{fp:d}f}'.format(fp=self.precision, val=self.attrs[key])
			except ValueError:
				# Now try the __str__
				svgattrs[key] = u'{val!s}'.format(val=self.attrs[key])
			except:
				raise

		svg = etree.Element(self.tag, svgattrs)
		if self.text is not None:
			svg.text = self.text

		if self.cdata is not None:
			# CDATA has to be added as a comment due to a
			# particularly dirty hack required by the output layer
			svg.append(etree.Comment(self.cdata))

		if type(self.subelements) == type(etree.Element('blank')):
			svg.append(self.subelements)
		elif self.subelements is not None:
			svg.extend(self.subelements)

		return svg