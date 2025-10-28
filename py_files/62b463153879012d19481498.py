def files_list(path):
	"""
	Return the files in given path.
	"""
	files = []
	for root, dirs, filenames in os.walk(path):
		for filename in filenames:
			file_path = os.path.join(root, filename)
			if file_path.endswith('.py'):
				files.append(file_path)

	return files