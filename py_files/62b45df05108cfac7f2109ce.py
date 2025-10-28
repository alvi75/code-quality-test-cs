def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if not self._is_ocfl(path):
		return False

	try:
		self.get_object(path)
	except Exception as e:
		return False

	return True