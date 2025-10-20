def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, dict):
		raise ValueError("Inventory must be a dictionary")
	
	if 'type' in inventory:
		type = inventory['type']
	else:
		type = None
	
	if type == None:
		if extract_spec_version:
			raise ValueError("No type found in inventory")
		else:
			spec_version = self.spec_version
	else:
		if type in self.type_map:
			spec_version = self.type_map[type]
		else:
			raise ValueError("Type %s not found" % type)

	if spec_version == 1:
		self.validate_v1(inventory)
	elif spec_version == 2:
		self.validate_v2(inventory)
	else:
		raise ValueError("Unknown specification version")