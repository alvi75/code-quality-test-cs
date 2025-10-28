def reset(self):
	"""
	Current context is reset to an empty dict, bins of the class are reinitialized with the *initial_value* or with *make_bins()*.
	"""
	self._context = {}
	if self.initial_value is not None:
		self._bins = make_bins(self.initial_value)
	else:
		self._bins = self.make_bins()