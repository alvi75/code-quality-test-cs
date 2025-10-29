def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = os.listdir(folder)
	xml_files = [f for f in files if f.endswith('.xml')]
	if len(xml_files) == 0:
		return None

	xml_files.sort()
	groups = []
	for xml_file in xml_files:
		group = _group_files_by_xml_filename(folder, xml_file)
		if group is not None:
			groups.append(group)

	return groups