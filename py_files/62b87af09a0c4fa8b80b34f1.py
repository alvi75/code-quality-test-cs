def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if not isinstance(coord, (int, float)):
		raise TypeError("coordinate must be a number")
	if self._bins is None:
		self._fill_bins()
	if coord < self._bins[0]:
		return
	elif coord > self._bins[-1]:
		return
	else:
		for i in range(len(self._bins)):
			if coord >= self._bins[i] and coord <= self._bins[i+1]:
				self._histogram[i] += weight