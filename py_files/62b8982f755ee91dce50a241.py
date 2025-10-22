def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	if self._normalized:
		return self

	self._normalized = True
	for unit in self.units:
		if isinstance(unit, TimeUnit):
			unit = unit.normalized
		elif isinstance(unit, list):
			unit = [x.normalized for x in unit]
		else:
			raise TypeError("Invalid type: %s" % type(unit))
		self.units[self.units.index(unit)] = unit
	return self