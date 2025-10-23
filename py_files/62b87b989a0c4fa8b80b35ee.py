def reset(self):
	"""
	Current context is reset to an empty dict, bins of the class are reinitialized with the *initial_value* or with *make_bins()*.
	"""
	self.context = {}
	if self.initial_value is not None:
		for bin in self.bins:
			self.context[bin] = self.initial_value
	else:
		self.make_bins()