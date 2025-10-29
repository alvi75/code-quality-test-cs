def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if self._is_root:
		return True

	if not os.path.exists(path):
		raise ValueError("Path %s does not exist" % path)

	if not os.path.isdir(path):
		raise ValueError("Path %s is not a directory" % path)

	return True