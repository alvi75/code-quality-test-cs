def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if extract_spec_version:
		if 'type' in inventory:
			if inventory['type'] in self.spec_versions:
				self.spec_version = self.spec_versions[inventory['type']]
			else:
				raise ValueError('Invalid type value: %s' % inventory['type'])
		else:
			raise ValueError('No type value found in inventory')
	else:
		if self.spec_version not in self.spec_versions:
			raise ValueError('Invalid specification version: %s' % self.spec_version)
		if 'type' not in inventory:
			raise ValueError('No type value found in inventory')
		if inventory['type'] != self.spec_versions[self.spec_version]:
			raise ValueError('Type value does not match specification version: %s' % inventory['type'])
		if 'id' not in inventory:
			raise ValueError('No id value found in inventory')
		if 'name' not in inventory:
			raise ValueError('No name value found in inventory')
		if 'version' not in inventory:
			raise ValueError('No version value found in inventory')
		if 'description' not in inventory:
			raise ValueError('No description value found in inventory')
		if 'license' not in inventory:
			raise ValueError('No license value found in inventory')
		if 'author' not in inventory:
			raise ValueError('No author value found in inventory')
		if 'author_email' not in inventory:
			raise ValueError('No author_email