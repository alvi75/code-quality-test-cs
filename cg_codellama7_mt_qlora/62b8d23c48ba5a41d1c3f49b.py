def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if self.size == 0:
		raise KeyError("popitem(): LRU cache is empty")
	key, value = self.cache.popitem(last=False)
	self.size -= 1
	return key, value