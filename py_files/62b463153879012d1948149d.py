def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	for filename in os.listdir(folder):
		if not filename.endswith(".xml"):
			continue
		group = _group_files_by_xml_filename(os.path.join(folder, filename))
		if group:
			yield group