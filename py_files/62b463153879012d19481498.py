def files_list(path):
	"""
	Return the files in given path.
	"""
	files = []
	for f in os.listdir(path):
		if not f.startswith('.'):
			files.append(f)
	return sorted(files)