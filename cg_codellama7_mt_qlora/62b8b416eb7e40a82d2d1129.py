def names(self, all=False):
	"""
	Return the attribute names of current class.
	"""
	if all:
		return self.all_names
	else:
		return self.names