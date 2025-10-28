def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, Inventory):
		raise TypeError("inventory must be of type Inventory")
	
	if extract_spec_version:
		spec_version = inventory.type
	else:
		spec_version = self.spec_version
		
	if spec_version == '1':
		self.validate_v1_inventory(inventory)
	elif spec_version == '2':
		self.validate_v2_inventory(inventory)