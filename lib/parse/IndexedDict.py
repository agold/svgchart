class IndexedDict(list):
	
	def __init__(self, items=None):

		list.__init__(self)
		self.__map = dict()

		try:
			# Try using items as a dict first
			for (key, value) in items.items():
				self.__setitem__(key, value)
		except AttributeError:
			# What a miserable failure. Try it as an iterable now
			if items is not None:
				for value in items:
					self.append(value)

	def __getitem__(self, key):

		if isinstance(key, int):
			# Key is an int--try to access in list
			return list.__getitem__(self, key)
		elif key in self.__map:
			# Not an int and does exist as a key in the map
			return self.__getitem__(self.__map[key])
		else:
			try:
				# If this value doesn't exist, raise an IndexError
				return self[0][key]
			except:
				raise IndexError("list index out of range")

	def __setitem__(self, key, value):

		if isinstance(key,int):
			# Key is an int--try to set it
			list.__setitem__(self, key, value)
		elif key not in self.__map:
			# Key doesn't exist, so throw it on the list and the map
			self.append(value)
			self.__map[key] = len(self) - 1
		else:
			# Key is already in the map, so overwrite its mapped value
			self.__setitem__(self.__map[key], value)

	def __getattr__(self,name):
		try:
			return getattr(self[0],name)
		except:
			raise AttributeError("No attribute " + name)

	def __str__(self):
		"""
		s = "{["
		for key in self.__map:
			s += str(key) + " : "
			s += str(self.__map[key]) + ","
		s += "]; ["
		for i in range(len(self)):
			s += str(i) + " : "
			s += str(self[i]) + ","
		s += "]} " """
		s = "InD{"
		if (len(self.keys()) == 0):
			for i in self:
				s += str(i) + ","
		else:
			for key in self.__map:
				s += str(key) + " : " + str(self[key]) + ","
		s += "}"
		return s

	def keys(self):
		return self.__map.keys()