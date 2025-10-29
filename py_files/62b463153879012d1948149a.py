def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	grouped = {}
	for file in files:
		xml_name = os.path.basename(file)
		if xml_name not in xmls:
			continue
		if xml_name not in grouped:
			grouped[xml_name] = []
		grouped[xml_name].append(file)

	return grouped