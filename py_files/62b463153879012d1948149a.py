def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	grouped = {}
	for file_name in files:
		xml_file = os.path.join(xmls, file_name)
		if not os.path.isfile(xml_file):
			continue

		xml_data = _read_xml(xml_file)
		if not xml_data:
			continue

		xml_data['file'] = file_name
		xml_data['xml_file'] = xml_file
		xml_data['source'] = source
		grouped[file_name] = xml_data

	return grouped