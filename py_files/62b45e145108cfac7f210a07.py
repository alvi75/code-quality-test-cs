def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, dict): # pragma: no cover
		raise Exception("Inventory must be a dictionary")
	self.inventory = inventory
	self.errors = []
	self.warnings = []

	# Check for missing required fields
	for field in self.required_fields:
		if not field in self.inventory: # pragma: no cover
			self.errors.append("Missing required field '%s'" % field)

	# Check for extra optional fields
	for field in self.optional_fields:
		if field in self.inventory: # pragma: no cover
			self.warnings.append("Extra optional field '%s' ignored" % field)

	# Check for extra non-optional fields
	for field in self.non_optional_fields:
		if field in self.inventory and not self.inventory[field]: # pragma: no cover
			self.warnings.append("Extra non-optional field '%s' ignored because it has a falsy value")

	# Check for invalid types if extracting spec version
	if extract_spec_version and 'type' in self.inventory: # pragma: no cover
		spec_version = self.inventory['type']
		if not spec_version in self.supported_versions: # pragma: no cover
			self.errors.append("Type '%s' is not supported by this library" % spec_version)
		else:
			self.spec_version = spec_version

	# Validate each item in the inventory
	for key, val in self.inventory.items():
		if key == "type": # pragma: no cover
			continue
		item = Item(key, val, self.spec_version)
		item.validate()
		self.errors += item.errors
		self.warnings += item.warnings

	return len(self.errors) == 0