def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if self._path is None:
		return False

	if self._path == path:
		return True

	if self._path.startswith(path):
		return True

	return False