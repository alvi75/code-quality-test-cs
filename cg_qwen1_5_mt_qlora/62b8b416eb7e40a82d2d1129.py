def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if not hasattr(self, '_names'):
			self._names = []
			for name in dir(self.__class__):
				if not name.startswith('_') or (name == 'self' and self is self.__class__.__dict__[name]):
					continue
				try:
					value = getattr(self, name)
					if isinstance(value, type) and value != self.__class__:
						continue
					elif isinstance(value, list):
						if len(value) > 0 and isinstance(value[0], type):
							continue
					self._names.append(name)
				except AttributeError:
					pass

		return self._names if not all else self._names[:]