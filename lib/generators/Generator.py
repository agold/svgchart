from lib.shapes.Shape import Shape
import re

class Generator(object):
	def __init__(self, data, settings):

		self.data = data
		self.settings = settings
		self.styles = {}

	def getCSS(self):
		self.getStyles()
		return Shape(tag=u'style', text=self.CSSString(), attrs={u'type': u'text/css'})

	def CSSString(self):
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
		classes = []
		for oneclass in classname.split():
			valid = re.match(r'^-?[_a-zA-Z]+[_a-zA-Z0-9-]*$', oneclass)
			if valid:
				classes.append('.' + oneclass)

		self.styles[', '.join(classes)] = self.__parseStyle(style)

	def addStyleToId(self, id=u'', style=u''):
		valid = re.match(r'^[a-zA-Z][-a-zA-Z0-9_:\.]*$', id)
		if valid:
			self.styles['#' + id] = self.__parseStyle(style)

	def addStyleToTag(self, tag, style):
		valid = re.match(r'^[a-zA-Z_:][-a-zA-Z0-9_:\.]*$', tag)
		if valid:
			self.styles[tag] = self.__parseStyle(style)

	def __parseStyle(self, style=''):
		styles = style.split(';')
		styledict = {}
		for pair in styles:
			if len(pair) > 0:
				key, value = pair.split(':')
				styledict[key.strip()] = value.strip()

		return styledict