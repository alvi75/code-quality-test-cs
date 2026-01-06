def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict) or 'files' not in fixity:
		return self.error('fixity', "Invalid fixity block: missing 'files' key")
	files = fixity['files']
	for file in files:
		if not isinstance(file, dict) or 'file' not in file:
			return self.error('fixity', "Invalid fixity block: 'files' contains invalid entries")
		file_name = file['file']
		if not os.path.isabs(file_name):
			file_name = os.path.join(os.getcwd(), file_name)
		if not os.path.exists(file_name):
			return self.error('fixity', "File '%s' does not exist" % file_name)
		if file_name not in manifest_files:
			return self.error('fixity', "File '%s' is not listed in the manifest" % file_name)

	return None