def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	grouped = {}
	for xml in xmls:
		xml_name = os.path.basename(xml)
		if not grouped.get(xml_name):
			grouped[xml_name] = []
		grouped[xml_name].append((source, xml, files))
	return grouped