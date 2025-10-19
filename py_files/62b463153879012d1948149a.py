def _group_files_by_xml_filename(source, xmls, files):
	"""
	Groups files by xmls and returns data in dict format.
	"""
	data = {}
	for xml in xmls:
		data[xml] = []
		for file in files:
			if source == "local":
				path = os.path.join(files_path, file)
			else:
				path = os.path.join(aws_s3_bucket, file)

			if path.endswith(xml):
				data[xml].append(file)

	return data