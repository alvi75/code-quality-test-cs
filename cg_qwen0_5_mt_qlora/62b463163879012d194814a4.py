def _explore_zipfile(zip_path):
	"""
	Groups the given zip path by using _group_files_by_xml_filename.
	"""
	for filename in _group_files_by_xml_filename(zip_path):
		yield filename, _read_file(zip_path, filename)