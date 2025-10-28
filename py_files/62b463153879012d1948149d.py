def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	group = []
	for filename in os.listdir(folder):
		if filename.endswith('.xml'):
			xml_file_path = os.path.join(folder, filename)
			group.append(_group_files_by_xml_filename(xml_file_path))
	return group