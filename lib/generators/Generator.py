from lib.shapes.Shape import Shape
import re

class Generator(object):
	"""Base class for a chart generator."""

	def __init__(self, data, settings):
		"""
		@param data: The parsed data to create the chart from
		@param settings: The settings used to format the chart
		"""

		self.data = data
		self.settings = settings
		self.styles = {}

	def getCSS(self):
		"""Returns a style element containing the style rules given in the settings document."""

		self.getStyles()
		return Shape(tag=u'style', text=self.CSSString(), attrs={u'type': u'text/css'})

	def CSSString(self):
		"""Collects all of the style strings."""

		cssstrings = []
		for key in self.styles:
			styles = self.styles[key]
			stylestrings = []
			for stylekey in styles:
				stylestrings.append(': '.join([stylekey, styles[stylekey]]))
			stylestring = '; '.join(stylestrings)
			cssstrings.append('{key} {{ {style}; }}'.format(key=key, style=stylestring))
		return "\n".join(cssstrings)


	def getStyles(self, section=None):
		"""Recursively retrieves the style information from a given section of the settings document.

		@param section: The section to search through
		"""

		if section is None:
			section = self.settings
		for setting in section:
			try:
				style = setting["style"]
				try:
					id = setting["id"]
					self.addStyleToId(id, style)
				except:
					classname = setting["class"]
					self.addStyleToClass(classname, style)
			except:
				pass
			for subsetting in setting:
				if isinstance(subsetting, list):
					self.getStyles(subsetting)
		return self.styles

	def addStyleToClass(self, classname=u'', style=u''):
		"""Applies a style to a given class name.

		@param classname: The classname to apply to
		@param style: The style string
		"""

		classes = []
		for oneclass in classname.split():
			valid = re.match(r'^-?[_a-zA-Z]+[_a-zA-Z0-9-]*$', oneclass)
			if valid:
				classes.append('.' + oneclass)

		self.styles[', '.join(classes)] = self.__parseStyle(style)

	def addStyleToId(self, id=u'', style=u''):
		"""Applies a style to a given ID tag.

		@param id: The ID to apply to
		@param style: The style string
		"""

		valid = re.match(r'^[a-zA-Z][-a-zA-Z0-9_:\.]*$', id)
		if valid:
			self.styles['#' + id] = self.__parseStyle(style)

	def addStyleToTag(self, tag, style):
		"""Applies a style to a given tag name.

		@param tag: The tag name to apply to
		@param style: The style string
		"""

		valid = re.match(r'^[a-zA-Z_:][-a-zA-Z0-9_:\.]*$', tag)
		if valid:
			self.styles[tag] = self.__parseStyle(style)

	def __parseStyle(self, style=''):
		"""Parses a style string into its constituent key:value pairs.

		@param style: The style string to parse
		"""

		styles = style.split(';')
		styledict = {}
		for pair in styles:
			if len(pair) > 0:
				key, value = pair.split(':')
				styledict[key.strip()] = value.strip()

		return styledict