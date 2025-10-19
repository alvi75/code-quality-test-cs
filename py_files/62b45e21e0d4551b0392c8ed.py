def find_path_type(path):
	"""
	Return a string indicating the type of thing at the given path
	"""
	if os.path.isdir(path) or os.path.islink(path):
		return "directory"
	elif os.path.isfile(path):
		return "file"
	else:
		return None