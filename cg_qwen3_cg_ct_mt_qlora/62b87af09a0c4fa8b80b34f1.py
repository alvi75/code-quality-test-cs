def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self._is_valid_coord(coord):
		self._data[self._get_index(coord)] += weight