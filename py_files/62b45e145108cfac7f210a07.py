def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, dict):
		raise ValueError("Inventory must be a dictionary.")
	
	if 'type' in inventory:
		if inventory['type'] == 'v1':
			self.validate_v1(inventory)
		elif inventory['type'] == 'v2':
			self.validate_v2(inventory)
		else:
			raise ValueError("Invalid type value: %s" % inventory['type'])
	else:
		if extract_spec_version:
			raise ValueError("No type value found in inventory.")
		else:
			self.validate_v1(inventory)