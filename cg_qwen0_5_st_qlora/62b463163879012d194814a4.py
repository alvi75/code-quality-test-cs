def _explore_zipfile(zip_path):
	"""
	Groups the given zip path by using _group_files_by_xml_filename.
	"""
	grouped = {}
	for filename in _group_files_by_xml_filename(zip_path):
		grouped[filename] = []
	for filename, files in grouped.items():
		yield filename, files