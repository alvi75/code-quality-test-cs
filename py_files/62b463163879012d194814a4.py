def _explore_zipfile(zip_path):
	"""
	Groups the given zip path by using _group_files_by_xml_filename.
	"""
	files = []
	for root, dirs, files in os.walk(zip_path):
		for file_name in files:
			file_path = os.path.join(root, file_name)
			if not file_path.endswith(".xml"):
				continue
			yield file_path