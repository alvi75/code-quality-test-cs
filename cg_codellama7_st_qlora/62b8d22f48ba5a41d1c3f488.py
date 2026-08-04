def popitem(self):
	"""
	Remove the value corresponding to the first inserted key and returns the key and value in tuple format.
	"""
	if self.size == 0:
		raise KeyError("popitem(): dictionary is empty")
	key = self.keys[0]
	value = self.values[0]
	del self.keys[0]
	del self.values[0]
	self.size -= 1
	return (key, value)