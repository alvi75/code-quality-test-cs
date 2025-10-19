def reset(self):
	"""
	Current context is reset to an empty dict, bins of the class are reinitialized with the *initial_value* or with *make_bins()*.
	"""
	self._context = {}
	for k in self._bins:
		if isinstance(self._bins[k], list):
			self._bins[k] = [self.initial_value() for i in range(len(self._bins[k]))]
		else:
			self._bins[k] = self.make_bins()
	return self