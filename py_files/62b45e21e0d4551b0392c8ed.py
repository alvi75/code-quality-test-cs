def find_path_type(path):
	"""
	Return a string indicating the type of thing at the given path
	"""
	if len(path) == 1:
		return 'file'
	elif len(path) == 2:
		return 'directory'
	else:
		raise ValueError('path must be one or two elements long')