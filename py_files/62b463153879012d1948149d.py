def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	groups = {}
	for filename, file in os.walk(folder).next():
		if not filename.startswith('.'):
			files = [f for f in os.listdir(filename) if f.endswith(".xml")]
			if len(files) > 0:
				groups[filename] = _group_files_by_xml_filename(os.path.join(filename, files))
	return groups