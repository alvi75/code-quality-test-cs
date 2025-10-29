def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	groups = []
	for filename in os.listdir(folder):
		if not filename.endswith('.xml'):
			continue
		xml_filename = os.path.join(folder, filename)
		with open(xml_filename) as f:
			xml = f.read()
		group = _group_files_by_xml_filename(xml)
		groups.append(group)

	return groups