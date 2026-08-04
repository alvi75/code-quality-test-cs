def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		self.error("Fixity block is not a dictionary")
		return
	if not isinstance(fixity.get('files'), list):
		self.error("Fixity block does not contain a list of files")
		return
	for file in fixity['files']:
		if not isinstance(file, dict):
			self.error("Fixity block contains a file that is not a dictionary")
			return
		if not isinstance(file.get('path'), str):
			self.error("Fixity block contains a file that does not have a path")
			return
		if not isinstance(file.get('checksum'), str):
			self.error("Fixity block contains a file that does not have a checksum")
			return
		if not isinstance(file.get('algorithm'), str):
			self.error("Fixity block contains a file that does not have an algorithm")
			return
		if not isinstance(file.get('size'), int):
			self.error("Fixity block contains a file that does not have a size")
			return
		if not isinstance(file.get('mimetype'), str):
			self.error("Fixity block contains a file that does not have a mimetype")
			return
		if not isinstance(file.get('created'), str):
			self.error("Fixity block contains a file that does not have a created date")
			return
		if not isinstance(file.get('modified'), str):
			self.error("Fixity block contains a file that does not have a modified date")
			return
		if not isinstance(file.get('format'), str):