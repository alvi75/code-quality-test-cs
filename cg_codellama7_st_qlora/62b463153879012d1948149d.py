def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = [f for f in os.listdir(folder) if f.endswith('.xml')]
	files.sort()
	groups = _group_files_by_xml_filename(files)
	return groups