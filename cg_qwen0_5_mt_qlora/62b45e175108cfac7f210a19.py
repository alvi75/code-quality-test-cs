def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict):
		raise TypeError("fixity must be a dictionary")
	for key in fixity:
		if not isinstance(key, str):
			raise TypeError("fixity keys must be strings")
		if key == "files":
			if not isinstance(fixity[key], list):
				raise TypeError("fixity files must be a list")
			for file in fixity[key]:
				if not isinstance(file, str):
					raise TypeError("fixity files must be a list of strings")
				if not os.path.exists(file):
					raise FileNotFoundError("Fixity file %s does not exist" % file)
				if not os.path.isfile(file):
					raise NotAFileError("Fixity file %s is not a file" % file)
				if not os.access(file, os.R_OK):
					raise PermissionError("Fixity file %s is not readable" % file)
				if not os.access(file, os.X_OK):
					raise PermissionError("Fixity file %s is not executable" % file)
				if not os.access(file, os.W_OK):
					raise PermissionError("Fixity file %s is not writable" % file)
		else:
			if not isinstance(fixity[key], str):
				raise TypeError("fixity values must be strings")