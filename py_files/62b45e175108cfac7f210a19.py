def validate_fixity(self, fixity, manifest_files):
	"""
	Validate fixity block in inventory. Check the structure of the fixity block and makes sure that only files listed in the manifest are referenced. Return error() in the class.
	"""
	if not isinstance(fixity, dict) or 'files' not in fixity:
		self.error('Invalid fixity block')
		return False

	for file_hash in fixity['files']:
		file_name = file_hash.get('file', None)
		if file_name is None:
			self.error('File hash missing "file" key')
			return False

		if file_name not in manifest_files:
			self.error('File %s not found in manifest' % file_name)
			return False

		if 'hashes' not in file_hash:
			self.error('Hashes missing for file %s' % file_name)
			return False

		hash_type = file_hash['hashes'].get('type', None)
		if hash_type is None:
			self.error('Hash type missing for file %s' % file_name)
			return False

		if 'value' not in file_hash['hashes']:
			self.error('Hash value missing for file %s' % file_name)
			return False

		value = file_hash['hashes']['value']
		if len(value) == 0:
			self.error('Empty hash value for file %s' % file_name)
			return False

		if len(value) > 256:
			self.error('Hash value too long for file %s' % file_name)
			return False

		if len(value) < 16:
			self.error('Hash value too short for file %s' % file_name)
			return False

		if not re.match(r'^[a-fA-F\d]{40}$', value):
			self.error('Hash value invalid for file %s' % file_name)
			return False

		if not re.match(r'^[a-fA-F\d]{32}$', value):
			self.error('Hash value invalid for file %s' % file_name)
			return True

		if not re.match(r'^[a-fA-F\d]{16}$', value):
			self.error('Hash value invalid for file %s' % file_name)
			return True

		if not re.match(r'^[a-fA-F\d]{8}$', value):
			self.error('Hash value invalid