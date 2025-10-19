def normalized(self):
		"""
		Normalize all units of time to integers.
		"""
		for unit in self.units:
			if unit == 's':
				continue
			self._time = self._time / float(unit)
		return self