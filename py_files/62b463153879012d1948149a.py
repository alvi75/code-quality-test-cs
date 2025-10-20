def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	xml_dict = {}
	for xml in xmls:
		xml_dict[xml] = []
	for file in files:
		if source == 'local':
			xml_dict[file['xml']].append(file)
		else:
			xml_dict[file['xml']].append(file['file'])
	return xml_dict