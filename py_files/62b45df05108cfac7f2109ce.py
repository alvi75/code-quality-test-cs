def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if self._root is None:
		return False

	if path == self._root.path:
		return True

	for child in self._children:
		if child.validate(path):
			return True

	return False