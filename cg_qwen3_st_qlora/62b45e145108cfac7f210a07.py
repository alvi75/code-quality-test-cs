def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, dict):
		raise ValueError('Inventory must be a dictionary')
	if 'type' not in inventory:
		raise ValueError('Inventory must have a "type" key')
	if not isinstance(inventory['type'], str):
		raise ValueError('Inventory "type" must be a string')
	if not self.is_valid_type(inventory['type']):
		raise ValueError('Invalid inventory type: %s' % inventory['type'])
	if extract_spec_version:
		self.spec_version = self.get_spec_version(inventory['type'])
	return self.validate_inventory(inventory)