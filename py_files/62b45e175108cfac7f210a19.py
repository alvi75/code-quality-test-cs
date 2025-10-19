def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not 'checksums' in fixity:
		self.error("Missing checksums", 2)
	elif not isinstance(fixity['checksums'], dict):
		self.error('Checksums is not a dictionary', 3)

	if not 'files' in fixity:
		self.error("Missing files", 4)
	elif not isinstance(fixity['files'], list):
		self.error('Files is not a list', 5)

	for f in fixity['files']:
		if not 'path' in f:
			self.error("Missing path for file", 6)
		elif not isinstance(f['path'], str):
			self.error('Path is not a string', 7)
		else:
			if not os.path.exists(f['path']):
				self.error("File does not exist: " + f['path'], 8)
			elif not f['path'] in manifest_files:
				self.error("File found but not in manifest: " + f['path'], 9)

	for k,v in fixity['checksums'].items():
		if not k in manifest_files:
			self.error("Checksum key found but not in manifest: " + k, 10)