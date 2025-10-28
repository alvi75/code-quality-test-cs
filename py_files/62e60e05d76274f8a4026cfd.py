def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if isinstance(key, str):
		key = key.strip()
		return self.indexes.get(key, None)
	else:
		return key