def status_str(self, prefix=''):
	"""
	Return string representation with self.log.status_str, with optional prefix.
	"""
	return self.log.status_str(prefix) + ' ' + self.log.status_str()