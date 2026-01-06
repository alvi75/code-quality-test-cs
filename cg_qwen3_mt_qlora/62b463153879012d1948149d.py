def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = os.listdir(folder)
	groups = {}
	for file in files:
		if file.endswith(".xml"):
			groups = _group_files_by_xml_filename(file, groups)
	return groups