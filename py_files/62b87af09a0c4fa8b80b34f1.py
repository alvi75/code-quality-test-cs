def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self._is_inside(coord) is False:
		return

	self._histogram[self._get_bin_index(coord)] += weight