def namesAndDescriptions(self, all=False):
		"""
		Returns the name and description of the current class attribute.
		"""
		if not self._isClass:
			return None

		names = []
		descriptions = []

		for attr in dir(self.__class__):
			if (not attr.startswith("__")) and \
			   (attr != "__init__") and \
			   (all or attr[0] == "_"):
				name = getattr(self.__class__, attr)
				descr = getattr(self.__class__, attr).__doc__
				if descr is not None:
					descr = descr.strip()
				names.append(name)
				descriptions.append(descr)

		return names, descriptions