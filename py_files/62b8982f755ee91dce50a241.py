def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	for unit in self.units:
		if isinstance(unit, TimeUnit):
			unit = unit.normalized()
		elif isinstance(unit, (int, float)):
			unit = int(unit)
		self._units[unit] = unit