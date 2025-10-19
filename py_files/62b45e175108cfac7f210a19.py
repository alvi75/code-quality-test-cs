def validate_fixity(self, fixity, manifest_files):
		"""
		def validate_fixity(self, fixity, manifest_files):
		Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
		"""
		if not isinstance(fixity, dict) or 'files' not in fixity:
			return self.error("Invalid fixity block", "Fixity block is missing 'files' key")
		for filename in fixity['files']:
			if filename not in manifest_files:
				return self.error("File '%s' not found" % (filename), "File '%s' not found in manifest" % (filename))
		return None