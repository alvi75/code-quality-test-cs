def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	grouped = {}
	for xml in xmls:
		if xml not in grouped:
			grouped[xml] = []
		grouped[xml].append(files)
	return grouped