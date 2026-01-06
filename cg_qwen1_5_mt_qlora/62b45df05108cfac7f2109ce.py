def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if not self._is_valid_path(path):
		return False

	try:
		self.get_object_info(path)
	except (OcflError, IOError) as e:
		return False

	return True