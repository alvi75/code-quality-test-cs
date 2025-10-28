def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, dict):
		raise ValueError("Inventory must be a dictionary")

	if 'type' in inventory:
		spec_version = inventory['spec_version']
	else:
		spec_version = self.spec_version

	if spec_version == 'D':
		return self.validate_d(inventory)

	elif spec_version == 'V':
		return self.validate_v(inventory)

	else:
		raise ValueError("Invalid specification version: %s" % spec_version)