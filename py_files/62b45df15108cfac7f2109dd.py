def status_str(self, prefix=''):
	"""
	Return string representation with self.log.status_str, with optional prefix.
	"""
	return '{0} {1}'.format(prefix, self.log.status_str())