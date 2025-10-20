def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict) or 'files' not in fixity:
		self.error("Invalid fixity block: %s" % fixity)
		return

	for file_hash in fixity['files']:
		file_path = os.path.join(self.inventory_dir, file_hash)

		if not os.path.exists(file_path):
			self.error("File does not exist: %s" % file_path)
			continue

		if file_path not in manifest_files:
			self.error("File is missing from manifest: %s" % file_path)
			continue