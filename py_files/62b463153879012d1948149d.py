def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = []
	for (dirpath, dirnames, filenames) in os.walk(folder):
		for filename in filenames:
			file_path = os.path.join(dirpath, filename)
			if not file_path.endswith(".xml"):
				continue
			file_name = file_path[:-4]
			files.append((file_name, file_path))
	return files