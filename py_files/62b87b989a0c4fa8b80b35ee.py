def reset(self):
	"""
	Current context is reset to an empty dict, bins of the class are reinitialized with the *initial_value* or with *make_bins()*. 
	"""
	self._context = {}
	if self._bins:
		for k in self._bins.keys():
			self._context[k] = self.make_bins()
	else:
		self._context = {}