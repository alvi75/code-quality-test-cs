def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = []
	for root, dirs, files in os.walk(folder):
		for file_name in files:
			file_path = os.path.join(root, file_name)
			if not file_path.endswith(".xml"):
				continue
			group = _group_files_by_xml_filename(file_path)
			files.append(group)
	return files