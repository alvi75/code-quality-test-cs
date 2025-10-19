def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if not self.is_root(path) and self.has_object(path):
		return True
	else:
		return False