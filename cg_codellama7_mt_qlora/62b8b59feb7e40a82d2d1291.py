def _getTargetClass(self):
	"""
	Define this to return the implementation in use,
without the 'Py' or 'Fallback' suffix.
	"""
	if self.implementation == 'Py':
		return self.implementation
	elif self.implementation == 'Fallback':
		return self.implementation
	else:
		return self.implementation.replace('Py', '').replace('Fallback', '')