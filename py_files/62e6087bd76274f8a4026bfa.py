def pop_u16(self):
	"""
	Remove the last two elements in self.data and return
	"""
	self._check_underflow(2)
	x = self.data[-2:]
	del self.data[-2:]
	return x[0]*256 + x[1]