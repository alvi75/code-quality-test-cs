def _explore_zipfile(zip_path):
	"""
	Groups the given zip path by using _group_files_by_xml_filename.
	"""
	groups = []
	for filename in os.listdir(zip_path):
		if filename.endswith('.xml'):
			groups.append(_group_files_by_xml_filename(os.path.join(zip_path, filename)))
	return groups