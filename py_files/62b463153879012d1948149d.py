def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = os.listdir(folder)
	xml_files = [f for f in files if f.endswith('.xml')]
	return _group_files_by_xml_filename(xml_files)