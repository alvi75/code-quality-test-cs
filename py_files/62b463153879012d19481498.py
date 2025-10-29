def files_list(path):
	"""
	Return the files in given path.
	"""
	files = []
	for root, dirs, files_ in os.walk(path):
		for f in files_:
			files.append(os.path.join(root, f))
	return files