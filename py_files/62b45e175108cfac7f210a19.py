def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		raise InvalidFixityBlock("fixity must be a dictionary")
	for file_name in fixity:
		if file_name not in manifest_files:
			self.error("File %s is missing from manifest" % file_name)