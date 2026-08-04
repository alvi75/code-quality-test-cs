def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	data = {}
	for xml in xmls:
		data[xml] = []
	for file in files:
		if file.endswith('.xml'):
			data[file].append(os.path.join(source, file))
	return data