def files_list(path):
	"""
	Return the files in given path.
	"""
	if not os.path.isdir(path):
		return [path]
	return [os.path.join(path, f) for f in os.listdir(path)]