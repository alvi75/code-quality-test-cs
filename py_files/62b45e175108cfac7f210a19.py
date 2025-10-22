def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		return self.error("Fixity block is not a dictionary")
	if 'algorithm' not in fixity:
		return self.error("Fixity block does not contain algorithm")
	if 'checksum' not in fixity:
		return self.error("Fixity block does not contain checksum")
	if 'files' not in fixity:
		return self.error("Fixity block does not contain files")

	for file in fixity['files']:
		if file not in manifest_files:
			return self.error("File %s is not in manifest" % file)