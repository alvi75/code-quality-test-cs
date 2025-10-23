def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""

	if not self._validate_path(path):
		return False

	try:
		self._validate_root(path)
	except Exception as e:
		print(e)
		return False

	return True