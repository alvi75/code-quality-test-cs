def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	groups = []
	for root, dirs, files in os.walk(folder):
		files = [os.path.join(root, f) for f in files]
		groups.append(_group_files_by_xml_filename(files))
	return groups