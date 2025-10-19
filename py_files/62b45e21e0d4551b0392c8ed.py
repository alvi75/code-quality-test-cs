def find_path_type(path):
	"""
	Return a string indicating the type of thing at the given path
	"""
	try:
		if os.path.isfile(path): return "file"
		if os.path.isdir(path): return "directory"
		if os.path.islink(path): return "symlink"
		return "unknown"
	except OSError: pass
	return "none"