def validate(self, inventory, extract_spec_version=False):
		"""
		Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
		"""
		if not isinstance(inventory, dict):
			raise TypeError("inventory must be of type dict")
		if not isinstance(self.spec_version, int):
			raise TypeError("specification version must be of type int")

		spec_version = None

		if extract_spec_version:
			spec_version = inventory.get('specification_version', 0)

		if spec_version == 1:
			return self.validate_v1(inventory)
		elif spec_version == 2:
			return self.validate_v2(inventory)
		else:
			raise ValueError("Invalid specification version: %s" % str(spec_version))