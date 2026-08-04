def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self.size == 0:
		raise KeyError("popitem(): dictionary is empty")
	
	key = self.keys[-1]
	value = self.values[-1]
	del self.keys[-1]
	del self.values[-1]
	self.size -= 1
	return (key, value)