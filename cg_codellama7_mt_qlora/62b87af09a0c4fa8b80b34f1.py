def fill(self, coord, weight=1):
	"""
	Fill histogram at *coord* with the given *weight*.

Coordinates outside the histogram edges are ignored.
	"""
	if self.is_empty():
		self.set_edges(coord)
		self.set_weight(weight)
		return
	if self.is_outside(coord):
		return
	if self.is_inside(coord):
		self.set_weight(self.get_weight() + weight)
		return
	if self.is_left_of(coord):
		self.left.fill(coord, weight)
		return
	if self.is_right_of(coord):
		self.right.fill(coord, weight)
		return
	if self.is_below(coord):
		self.below.fill(coord, weight)
		return
	if self.is_above(coord):
		self.above.fill(coord, weight)
		return