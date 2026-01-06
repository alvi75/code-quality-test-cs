def _explore_zipfile(zip_path):
	"""
	Groups the given zip path by using _group_files_by_xml_filename.
	"""
	with zipfile.ZipFile(zip_path) as zf:
		return _group_files_by_xml_filename(zf.namelist())