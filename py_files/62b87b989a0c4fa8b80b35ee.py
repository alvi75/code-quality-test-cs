def reset(self):
	"""
	Current context is reset to an empty dict, bins of the class are reinitialized with the *initial_value* or with *make_bins()*.
	"""
	self._context = {}
	if self.make_bins:
		self.bins = make_bins(self.initial_value)