def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if self.curr is None:
		raise KeyError("popitem(): cache is empty")
	key, value = self.curr.key, self.curr.value
	self.curr = self.curr.prev
	self.curr.next = None
	self.size -= 1
	return key, value