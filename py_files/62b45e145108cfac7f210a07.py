def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, Inventory):
		raise TypeError("inventory must be an instance of Inventory")
	if not isinstance(extract_spec_version, bool):
		raise TypeError("extract_spec_version must be a boolean")

	for item in inventory.items:
		if not isinstance(item, Item):
			raise TypeError("item must be an instance of Item")
		if not isinstance(item.type, str):
			raise TypeError("type must be a string")
		if not isinstance(item.version, str):
			raise TypeError("version must be a string")
		if not isinstance(item.spec_version, str):
			raise TypeError("spec_version must be a string")
		if not isinstance(item.spec_type, str):
			raise TypeError("spec_type must be a string")
		if not isinstance(item.spec_version, str):
			raise TypeError("spec_version must be a string")