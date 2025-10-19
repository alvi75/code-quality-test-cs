def status_str(self, prefix=''):
		"""Return string representation with self.log.status_str, with optional prefix."""
		if not prefix:
			prefix = ''
		return '%s%s: %s' % (prefix, self.log.prefix, self.log.status_str)