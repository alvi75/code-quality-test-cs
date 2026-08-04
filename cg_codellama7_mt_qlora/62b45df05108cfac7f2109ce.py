def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if path == '/':
		return True
	elif self.fs.exists(path):
		return self.fs.isdir(path)
	else:
		return False