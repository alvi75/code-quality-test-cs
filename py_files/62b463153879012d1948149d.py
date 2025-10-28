def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	for filename in os.listdir(folder):
		if filename.endswith(".xml"):
			group = _group_files_by_xml_filename(os.path.join(folder, filename))
			yield group