def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if key in self.keys:
		return self.keys.index(key)
	else:
		return -1