def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	if self._normalized:
		return self

	self._normalized = True
	for unit in self.units:
		unit.normalize()
	return self