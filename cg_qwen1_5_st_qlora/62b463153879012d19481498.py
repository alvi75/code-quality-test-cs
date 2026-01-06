def files_list(path):
	"""
	Return the files in given path.
	"""
	files = []
	for root, dirs, filenames in os.walk(path):
		for filename in filenames:
			filepath = os.path.join(root, filename)
			if filepath.endswith('.py'):
				files.append(filepath)

	return files