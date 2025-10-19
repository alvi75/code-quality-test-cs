def pop_u16(self):
	"""
	Remove the last two elements in self.data and return
	"""
	self.data.pop()
	self.data.pop()
	return struct.unpack("<H", self.data[-2:])[0]