def find_path_type(path):
	"""
	Return a string indicating the type of thing at the given path
	"""
	if os.path.isfile(path) or os.path.islink(path):
		return 'file'
	elif os.path.isdir(path):
		return 'dir'
	else:
		raise ValueError('Invalid path: %s' % (path,))