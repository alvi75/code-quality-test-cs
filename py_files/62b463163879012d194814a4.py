def _explore_zipfile(zip_path):
	"""
	Groups the given zip file by using _group_files_by_xml_filename.
	"""
	zip_file = zipfile.ZipFile(zip_path, 'r')
	file_names = zip_file.namelist()
	files_by_xml_filename = _group_files_by_xml_filename(file_names)
	return files_by_xml_filename