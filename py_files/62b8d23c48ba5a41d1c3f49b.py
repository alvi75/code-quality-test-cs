def popitem(self):
	"""
	"Remove and return the (key, value) pair most recently used.
	"""
	if len(self._queue) == 0:
		raise IndexError("pop from empty queue")
	return self._queue.pop(), self._dict.pop(self._queue[-1][0])