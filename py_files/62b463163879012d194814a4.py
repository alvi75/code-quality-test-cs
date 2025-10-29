def _explore_zipfile(zip_path):
	"""
	Groups the given zip path by using _group_files_by_xml_filename.
	"""
	groups = {}
	for filename in _get_filenames_from_zip(zip_path):
		if filename not in groups:
			groups[filename] = []
		groups[filename].append(filename)
	return groups