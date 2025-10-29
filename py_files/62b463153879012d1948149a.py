def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	xml_dict = {}
	for xml in xmls:
		xml_dict[xml] = []
	for file in files:
		if file.endswith('.xml'):
			xml_dict[file].append(file)
	return xml_dict