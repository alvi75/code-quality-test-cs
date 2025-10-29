def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if not isinstance(key, int):
		key = self._indexer[key]
	return key