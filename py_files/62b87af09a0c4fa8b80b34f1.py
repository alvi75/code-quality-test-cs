def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if not self._valid_coord(coord): return
	self._data.setdefault(tuple(coord), 0)
	self[tuple(coord)] += weight