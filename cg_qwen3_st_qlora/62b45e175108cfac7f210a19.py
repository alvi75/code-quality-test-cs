def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("Fixity block is not a dictionary.")
		return

	if "algorithm" not in fixity:
		self.error("Fixity block does not contain 'algorithm' key.")
		return

	if "value" not in fixity:
		self.error("Fixity block does not contain 'value' key.")
		return

	if "files" not in fixity:
		self.error("Fixity block does not contain 'files' key.")
		return

	if not isinstance(fixity["files"], list):
		self.error("Fixity block 'files' key is not a list.")
		return

	for file in fixity["files"]:
		if not isinstance(file, dict):
			self.error("Fixity block 'files' key contains non-dictionary item.")
			return

		if "path" not in file:
			self.error("Fixity block 'files' key contains no 'path' key.")
			return

		if "hash" not in file:
			self.error("Fixity block 'files' key contains no 'hash' key.")
			return

		if not isinstance(file["path"], str):
			self.error("Fixity block 'files' key contains non-string 'path' value.")
			return

		if not isinstance(file["hash"], str):
			self.error("Fixity block 'files' key contains non-string 'hash' value.")
			return

		if file["path"] not in manifest_files:
			self.error("Fixity block references file '%s' which is not in manifest." % file["path"])
			return

		if file["hash"] != self.hash_file(file["path"], fixity["algorithm"]):
			self.error("Fixity block hash for file '%s' does not match actual hash." % file["path"])
			return