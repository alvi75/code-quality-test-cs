def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	grouped = {}
	for xml in xmls:
		xml_name = os.path.basename(xml)
		if not grouped.has_key(xml_name):
			grouped[xml_name] = []
		for file in files:
			file_name = os.path.basename(file)
			if file_name.startswith(xml_name) and file_name.endswith(".txt"):
				grouped[xml_name].append((file, source))
	return grouped