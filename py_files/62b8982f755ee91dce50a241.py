def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	for unit in self.units:
		if isinstance(unit, TimeUnit):
			unit.normalize()
	return self