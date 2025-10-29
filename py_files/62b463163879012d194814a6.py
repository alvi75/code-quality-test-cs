def files_list_from_zipfile(zip_path):
	"""
	Return the files in the given zip path.
	"""
	with zipfile.ZipFile(zip_path) as zf:
		return [f for f in zf.namelist()]