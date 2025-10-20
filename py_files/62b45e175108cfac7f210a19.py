def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict) or 'files' not in fixity:
		return self.error('fixity block is not a dictionary with key "files"')
	for file in fixity['files']:
		if not isinstance(file, dict) or 'path' not in file or 'hashes' not in file:
			return self.error('fixity block has invalid format')
		if file['path'] not in manifest_files:
			return self.error('fixity block references non-existent file')