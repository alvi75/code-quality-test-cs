def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, dict):
		raise ValueError("Inventory must be a dictionary")
	
	if 'type' in inventory:
		if inventory['type'] == '1':
			self.spec_version = '1'
		elif inventory['type'] == '2':
			self.spec_version = '2'
		else:
			raise ValueError("Invalid type value: %s" % inventory['type'])
	else:
		if extract_spec_version:
			raise ValueError("No type value found in inventory.")
		else:
			self.spec_version = '1'

	if self.spec_version == '1':
		return self.validate_v1(inventory)
	else:
		return self.validate_v2(inventory)