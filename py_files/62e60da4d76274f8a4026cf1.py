def values(self, *keys):
	'''
	Returns the key filtered by self.index in the form of a list.
	'''
	if len(keys) == 0:
		return [self._index[key] for key in keys]
	else:
		values = []
		for key in keys:
			values.append(self._index[key])
		return values