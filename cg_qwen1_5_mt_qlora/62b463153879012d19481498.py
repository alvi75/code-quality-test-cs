def files_list(path):
	"""
	Return the files in given path.
	"""
	if not os.path.exists(path):
		return []
	files = [os.path.join(path, f) for f in os.listdir(path)]
	for i, file in enumerate(files):
		if os.path.isdir(file):
			files[i] = files_list(file)
	return files