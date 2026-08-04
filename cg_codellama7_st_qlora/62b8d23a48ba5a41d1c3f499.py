def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self.size == 0:
		raise KeyError("popitem(): cache is empty")
	
	# remove the least recently used item
	key = self.lru_list.pop()
	value = self.cache.pop(key)
	
	# update the cache
	self.size -= 1
	
	return (key, value)