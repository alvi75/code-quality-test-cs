def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("fixity must be a dictionary")
	if "algorithm" not in fixity:
		self.error("fixity must contain 'algorithm' key")
	if "files" not in fixity:
		self.error("fixity must contain 'files' key")
	for file in fixity["files"]:
		if file not in manifest_files:
			self.error("fixity references non-existent file: %s" % file)