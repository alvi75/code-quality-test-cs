def index(self, key):
	"""
	Returns the key in the form of int.
	"""
	if key not in self.keys:
		raise KeyError("Key %s not found in the dictionary" % key)
	return self.keys.index(key)