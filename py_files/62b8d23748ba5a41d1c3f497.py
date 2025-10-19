def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self._items:
		key, value = next(six.iteritems(heapq.heappop(self._freq_to_items)))
		del self._items[key]
		return key, value
	else:
		raise KeyError('No items')