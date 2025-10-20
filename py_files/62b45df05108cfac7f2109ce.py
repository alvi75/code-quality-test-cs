def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if self._validate_path(path):
		return True
	else:
		self.logger.error("Path %s is not a valid OCFL object", path)
		return False