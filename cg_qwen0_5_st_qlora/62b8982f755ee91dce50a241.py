def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	for unit in self.units:
		unit.normalize()
	return self