def _explore_folder(folder):
	"""
	Groups files in the given group by using _group_files_by_xml_filename.
	"""
	files = {}
	for filename in os.listdir(folder):
		if not (filename.endswith(".xml") or filename.endswith(".XML")):
			continue

		parts = filename.split("_")
		if len(parts) != 2:
			continue

		xml_group, xml_id = parts
		if xml_group not in files:
			files[xml_group] = {}

		files[xml_group][int(xml_id)] = os.path.join(folder, filename)

	return files