def popitem(self):
	"""
	Remove and return the `(key, value)` pair least frequently used.
	"""
	if self.size == 0:
		raise KeyError("popitem(): lru cache is empty")
	
	# find the least frequently used item
	least_frequently_used_item = None
	least_frequency = None
	for key, value in self.items():
		if least_frequently_used_item is None or value.frequency < least_frequency:
			least_frequently_used_item = key
			least_frequency = value.frequency
	
	# remove the item
	del self[least_frequently_used_item]
	return least_frequently_used_item