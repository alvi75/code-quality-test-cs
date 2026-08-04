def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("fixity block must be a dictionary")
	if not 'files' in fixity:
		self.error("fixity block must have a 'files' key")
	if not isinstance(fixity['files'], list):
		self.error("fixity block 'files' key must be a list")
	for f in fixity['files']:
		if not isinstance(f, dict):
			self.error("fixity block 'files' key must be a list of dictionaries")
		if not 'path' in f:
			self.error("fixity block 'files' key must have a 'path' key")
		if not isinstance(f['path'], str):
			self.error("fixity block 'files' key 'path' must be a string")
		if not 'algorithm' in f:
			self.error("fixity block 'files' key must have an 'algorithm' key")
		if not isinstance(f['algorithm'], str):
			self.error("fixity block 'files' key 'algorithm' must be a string")
		if not 'checksum' in f:
			self.error("fixity block 'files' key must have a 'checksum' key")
		if not isinstance(f['checksum'], str):
			self.error("fixity block 'files' key 'checksum' must be a string")
		if not f['path'] in manifest_files:
			self.error("fixity block 'files' key 'path' must be a file listed in the manifest")