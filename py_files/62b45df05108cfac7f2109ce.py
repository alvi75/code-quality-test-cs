def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if not self._pyfs:
		return False

	try:
		self._pyfs.stat(path)
	except OSError as e:
		if e.errno == errno.ENOENT:
			return False
		raise

	return True