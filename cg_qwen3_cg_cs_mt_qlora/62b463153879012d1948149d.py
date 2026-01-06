def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = []
	for root, dirs, filenames in os.walk(folder):
		for filename in fnmatch.filter(filenames, '*.xml'):
			files.append(os.path.join(root, filename))
	return _group_files_by_xml_filename(files)