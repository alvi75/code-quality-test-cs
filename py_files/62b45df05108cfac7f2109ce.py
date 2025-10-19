def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if self.is_ocfl_root(path=path) or self.is_pyfs_root(path=path):
		return True
	else:
		return False