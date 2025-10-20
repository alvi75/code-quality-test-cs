def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = os.listdir(folder)
	groups = {}
	for file in files:
		if not file.endswith(".xml"):
			continue

		xml_file = os.path.join(folder, file)
		group = _group_files_by_xml_filename(xml_file)

		if group is None:
			continue

		if group not in groups:
			groups[group] = []

		groups[group].append(file)

	return groups