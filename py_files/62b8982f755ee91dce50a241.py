def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	if self._normalized:
		return self

	self._normalized = True
	for unit in self.units:
		if unit == 's':
			continue
		value = getattr(self, unit)
		if value is not None:
			setattr(self, unit, int(value))
	return self