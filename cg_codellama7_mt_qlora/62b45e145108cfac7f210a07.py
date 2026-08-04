def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if extract_spec_version:
		if 'type' in inventory:
			if inventory['type'] in self.spec_versions:
				self.spec_version = inventory['type']
			else:
				raise ValueError('Invalid type value: %s' % inventory['type'])
		else:
			raise ValueError('No type value found')
	else:
		if self.spec_version not in self.spec_versions:
			raise ValueError('Invalid specification version: %s' % self.spec_version)
	if 'id' not in inventory:
		raise ValueError('No id value found')
	if 'name' not in inventory:
		raise ValueError('No name value found')
	if 'description' not in inventory:
		raise ValueError('No description value found')
	if 'version' not in inventory:
		raise ValueError('No version value found')
	if 'author' not in inventory:
		raise ValueError('No author value found')
	if 'license' not in inventory:
		raise ValueError('No license value found')
	if 'type' not in inventory:
		raise ValueError('No type value found')
	if 'spec_version' not in inventory:
		raise ValueError('No spec_version value found')
	if 'created' not in inventory:
		raise ValueError('No created value found')
	if 'modified' not in inventory:
		raise ValueError('No modified value found')
	if 'inventory' not in inventory:
		raise ValueError('No inventory value found')
	if 'groups' not in inventory:
		raise ValueError('No