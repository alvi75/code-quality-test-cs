def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""

	if not isinstance(inventory, dict):
		raise TypeError("Inventory must be a dictionary")

	for key, val in inventory.items():
		if not isinstance(key, str) or not isinstance(val, list):
			raise TypeError("Inventory keys/values must be strings/lists")
		elif len(val) == 0:
			raise ValueError("Inventory lists cannot be empty")