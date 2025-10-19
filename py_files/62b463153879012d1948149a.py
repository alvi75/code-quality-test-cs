def _group_files_by_xml_filename(source, xmls, files):
		"""
		Groups files by xmls and returns data in dict format.
		"""
		grouped = {}
		for filename in files:
			xml_name = os.path.splitext(filename)[0] + '.xml'
			if xml_name in xmls:
				grouped[filename] = source
		return grouped