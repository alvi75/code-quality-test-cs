def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if self._is_root(path):
		return True

	try:
		with open(path) as f:
			return True
	except IOError:
		return False