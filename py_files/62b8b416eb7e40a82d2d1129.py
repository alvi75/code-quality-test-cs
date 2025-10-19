def names(self, all=False):
		"""
		Return the attribute names of current class.
		"""
		names = []
		for name in self.__dict__:
			if not name.startswith('__') and hasattr(self, name) and \
			   isinstance(getattr(self, name), Attribute):
				names.append(name)
		return names if all else False