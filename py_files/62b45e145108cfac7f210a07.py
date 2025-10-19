def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, list):
		raise TypeError("inventory must be a list")
	for item in inventory:
		if not isinstance(item, dict):
			raise TypeError("item must be a dictionary")
		if "type" not in item:
			raise ValueError("item must have 'type' key")
		if extract_spec_version:
			type_value = item["type"]
			if type_value == "specification":
				return True
			elif type_value == "specification-version-1":
				return True
			else:
				raise ValueError("Invalid type value: %s" % type_value)
		else:
			pass
		return True
	return False