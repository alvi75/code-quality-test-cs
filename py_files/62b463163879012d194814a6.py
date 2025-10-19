def files_list_from_zipfile(zip_path):
	"""
	Return the files in the given zip path.
	"""
	zip_file = zipfile.ZipFile(zip_path)
	return [zip_file.namelist()[i] for i in range(len(zip_file.namelist()))]