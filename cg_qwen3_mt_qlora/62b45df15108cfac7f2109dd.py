def status_str(self, prefix=''):
	"""
	Return string representation with self.log.status_str, with optional prefix.
	"""
	return prefix + ' '.join([self.log.status_str, str(self)])