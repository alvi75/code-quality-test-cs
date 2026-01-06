def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self._is_empty:
		return

	for i in range(len(coord)):
		self._hist[i].fill(coord[i], weight)