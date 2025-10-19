def files_list_from_zipfile(zip_path):
	"""
	Return the files in the given zip path.
	"""
	files = []
	with zipfile.ZipFile(zip_path) as z:
		for name in z.namelist():
			if not name.startswith("/"):
				name = "/" + name
			files.append(name)
	return files