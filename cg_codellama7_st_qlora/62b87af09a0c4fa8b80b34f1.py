def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self.is_empty():
		return
	if self.is_1d():
		self.fill_1d(coord, weight)
	else:
		self.fill_2d(coord, weight)