def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""

	if not isinstance(fixity, dict):
		return self.error("Fixity block is not a dictionary")

	if "fixity" not in fixity:
		return self.error("Missing 'fixity' key in fixity block")

	fixity = fixity["fixity"]

	if not isinstance(fixity, dict):
		return self.error("'fixity' key in fixity block is not a dictionary")

	if "algorithm" not in fixity:
		return self.error("Missing 'algorithm' key in fixity block")

	if "checksum" not in fixity:
		return self.error("Missing 'checksum' key in fixity block")

	if "files" not in fixity:
		return self.error("Missing 'files' key in fixity block")

	if not isinstance(fixity["files"], list):
		return self.error("'files' key in fixity block is not a list")

	for file in fixity["files"]:
		if not isinstance(file, dict):
			return self.error("File entry in 'files' key in fixity block is not a dictionary")
		if "path" not in file:
			return self.error("Missing 'path' key in file entry in 'files' key in fixity block")
		if "checksum" not in file:
			return self.error("Missing 'checksum' key in file entry in 'files' key in fixity block")
		if file["path"] not in manifest_files:
			return self.error("File entry in 'files' key in fixity block references a file not in manifest: %s" % file["path"])