def validate_fixity(self, fixity, manifest_files):
		"""def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, list):
		return self.error("fixity must be a list")
	for f in fixity:
		if not isinstance(f, dict):
			return self.error("fixity items must be dicts")

	fixity_items = []
	for item in fixity:
		if 'file' in item:
			if not os.path.isfile(item['file']):
				return self.error('File %s does not exist.' % (item['file']))
			elif not os.access(item['file'], os.R_OK):
				return self.error('File %s is not readable.' % (item['file']))

			if item['file'] not in manifest_files:
				return self.error('File %s was not found in manifest.' % (item['file']))

			fixity_items.append(item)
		else:
			return self.error('Fixity item must have key \'file\'.')

	return None