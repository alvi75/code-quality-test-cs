def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	for filename in os.listdir(folder):
		if not filename.endswith('.xml'):
			continue

		xml_filename = os.path.join(folder, filename)
		group = _group_files_by_xml_filename(xml_filename)

		for file_name, file_path in group.items():
			file_path = os.path.join(folder, file_name)
			yield file_path