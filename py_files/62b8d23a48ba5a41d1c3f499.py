def popitem(self):
	"""
	Remove and return the `(key, value)` pair least recently used.
	"""
	if not self._queue:
		raise KeyError("pop from empty queue")
	key = self._queue[0][0]
	value = self._queue[0][1]
	self._queue.pop(0)
	return key, value