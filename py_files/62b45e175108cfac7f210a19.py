def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		return self.error("fixity must be a dictionary")

	for file_name in manifest_files:
		if file_name not in fixity:
			return self.error("manifest does not contain file %s" % file_name)

	return True