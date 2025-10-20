def pop_u16(self):
	"""
	Remove the last two elements in self.data and return
	"""
	if len(self.data) < 2:
		raise ValueError("pop from empty list")
	return self.data.pop() | (self.data[-1] << 8)