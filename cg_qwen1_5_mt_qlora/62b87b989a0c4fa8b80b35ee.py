def reset(self):
	"""
	Current context is reset to an empty dict, bins of the class are reinitialized with the *initial_value* or with *make_bins()*. 
	"""
	self._context = {}
	for k in self.bins.keys():
		if isinstance(k, str) and k.startswith('_'):
			continue
		else:
			self._context[k] = self.initial_value.copy()
	return self