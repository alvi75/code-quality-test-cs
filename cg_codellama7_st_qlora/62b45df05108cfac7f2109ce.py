def validate(self, path):
	"""
	Returns True if OCFL object at path or pyfs root, False otherwise.
	"""
	if path == self.root:
		return True
	elif path in self.objects:
		return True
	else:
		return False