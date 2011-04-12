class Shape(object):
	"""Base class of a generic shape."""

	attrs = {}
	tagName = None
	innerValue = None
	precision = 4

	def __init__(self, attrs={}, **kwargs):
		self.attrs = dict(attrs, **kwargs)

	@property
	def svg(self):
		if self.tagName is not None:
			svg = [u'<{tag:s}'.format(tag=self.tagName)]
			for key in self.attrs.keys():
				svg += [u'{key:s}="{value}"'.format(
						key=key, value=self.attrs[key])]

			if self.innerValue is not None:
				svg += [u'>{inner}</{tag:s}>'.format(
						inner=self.innerValue, tag=self.tagName)]
			else:
				svg += [u'/>']

			return u' '.join(svg)