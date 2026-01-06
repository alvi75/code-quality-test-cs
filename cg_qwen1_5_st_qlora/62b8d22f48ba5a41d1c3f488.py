def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	key = self.keys()[0]
	value = self.values()[0]
	del self[key]
	return (key, value)