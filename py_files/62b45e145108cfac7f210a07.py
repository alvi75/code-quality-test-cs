def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, dict):
		raise ValueError("Inventory must be a dictionary")

	for key in inventory:
		if key == "type":
			if not isinstance(inventory[key], str):
				raise ValueError("Type must be a string")
			if inventory[key] != "spec" and inventory[key] != "extract":
				raise ValueError("Invalid type value: %s" % inventory[key])
		elif key == "version":
			if not isinstance(inventory[key], int):
				raise ValueError("Version must be an integer")
			if inventory[key] < 1:
				raise ValueError("Version must be greater than zero")
		else:
			raise ValueError("Unknown key: %s" % key)

	if extract_spec_version:
		spec_version = inventory.get("spec_version", None)
		if spec_version is None:
			raise ValueError("No specification version specified")
		if not isinstance(spec_version, int):
			raise ValueError("Spec version must be an integer")
		if spec_version < 0:
			raise ValueError("Spec version must be greater than zero")