def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self._edges is None:
		raise RuntimeError("Histogram has no edges")
	for i in range(len(coord)):
		if not (self._edges[i] <= coord[i] < self._edges[i+1]):
			continue
		self._histogram[i].fill(coord[i], weight)