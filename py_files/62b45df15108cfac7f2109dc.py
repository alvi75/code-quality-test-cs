def status_str(self, prefix=''):
	"""
	Return a string with visiting the sorted self.messages list, each visit add prefix and the element in the sorted self.messages list.
	"""
	return ''.join([prefix + str(m) for m in sorted(self.messages)])