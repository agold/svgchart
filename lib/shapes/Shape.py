import xml.etree.ElementTree as etree

class Shape(object):
	"""Base class of a generic shape.

	Public methods:
	__str__() -- returns the SVG representation as a string
	svg() -- returns the SVG representation as an XML fragment

	Examples:
	>>> shape = Shape('foo', 'bar', attrs={'spoons': 'forks'}, knives='sharp')
	>>> shape.tag
	'foo'
	>>> shape.text
	'bar'
	>>> shape.attrs
	{'spoons': 'forks', 'knives': 'sharp'}
	>>> print shape
	<foo knives="sharp" spoons="forks">bar</foo>

	"""

	def __init__(self, tag=u'', text=None, precision=4, attrs={}, **kwargs):
		"""Keyword arguments:
		tag -- the SVG tag name
		text -- inner text of the SVG element
		precision -- the decimal precision for numbers in SVG output
		attrs -- dictionary of key-value pairs for the SVG element's attributes

		"""

		self.tag = tag
		self.text = text
		self.precision = precision
		self.attrs = dict(attrs, **kwargs)

	def __str__(self):
		"""Returns the SVG representation as a string."""

		return etree.tostring(self.svg(), encoding='utf-8')
	
	def svg(self):
		"""Returns the SVG representation as an XML fragment."""

		svgattrs = {}
		for key in self.attrs.keys():
			try:
				# Attemt to format as float with given precision
				svgattrs[key] = u'{val:.{fp:d}f}'.format(fp=self.precision, val=self.attrs[key])
			except ValueError:
				# Now try the __str__
				svgattrs[key] = u'{val!s}'.format(val=self.attrs[key])
			except:
				raise
			
		svg = etree.Element(tag=self.tag, attrib=svgattrs)
		if self.text is not None:
			svg.text = self.text
		
		return svg