def _group_files_by_xml_filename(source, xmls, files):
		"""
		Groups files by xmls and returns data in dict format.
		"""
		result = {}
		for file in files:
			if not os.path.isfile(file):
				continue

			filename = os.path.basename(file)
			filename_without_extension = filename.split('.')[0]
			xml_name = filename_without_extension + '.xml'

			if xml_name not in xmls:
				continue

			if xml_name not in result:
				result[xml_name] = []

			result[xml_name].append({
				'filename': filename,
				'source': source,
				'xmls': [xml_name],
				'files': [file]
			})

		return result

	# Get all files from a directory
	def get_all_files(directory):
		files = []
		for root, _, filenames in os.walk(directory):
			for filename in filenames:
				file_path = os.path.join(root, filename)
				files.append(file_path)

		return files

	# Get all .xml files from a directory
	def get_xml_files(directory):
		files = []
		for root, _, filenames in os.walk(directory):
			for filename in filenames:
				file_path = os.path.join(root, filename)
				if file_path.endswith('.xml'):
					files.append(file_path)

		return files

	# Get all .xml files from a directory recursively
	def recursive_get_xml_files(directory):
		files = []
		for root, _, filenames in os.walk(directory):
			for filename in filenames:
				file_path = os.path.join(root, filename)
				if file_path.endswith('.xml'):
					files.append(file_path)

		return files

	# Get all .xml files from a directory and its subdirectories
	def get_all_xml_files(directory):
		files = []
		for root, _, filenames in os.walk(directory):
			for filename in filenames:
				file_path = os.path.join(root, filename)
				if file_path.endswith('.xml'):
					files.append(file_path)

		return files

	# Get all .xml files from a directory and its subdirectories recursively
	def recursive_get_all_xml_files(directory):
		files = []
		for root, _, filenames in os.walk(directory):
			for filename in filenames:
				file_path = os.path.join(root, filename)
				if file_path.endswith('.xml'):
					files.append(file_path)

		return files

	# Get all .xml files from a directory and its sub