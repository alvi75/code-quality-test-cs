def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		return self.error("fixity must be a dictionary")
	if "files" not in fixity:
		return self.error("fixity must have a 'files' key")
	for file_name in fixity["files"]:
		if file_name not in manifest_files:
			return self.error("file '%s' is not in the manifest" % file_name)