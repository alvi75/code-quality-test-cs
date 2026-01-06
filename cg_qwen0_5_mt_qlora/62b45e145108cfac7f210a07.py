def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not self.spec_version:
		self.spec_version = self.get_spec_version(inventory)

	if extract_spec_version:
		spec_version = self.spec_version
	else:
		spec_version = self.spec_version

	if spec_version != inventory.spec_version:
		raise ValueError("Inventory has different spec version than expected: %s" % spec_version)

	for key, value in six.iteritems(inventory):
		if isinstance(value, dict):
			self.validate_dict(value, spec_version=spec_version)
		elif isinstance(value, list):
			self.validate_list(value, spec_version=spec_version)
		elif isinstance(value, tuple):
			self.validate_tuple(value, spec_version=spec_version)
		elif isinstance(value, set):
			self.validate_set(value, spec_version=spec_version)
		elif isinstance(value, str):
			pass
		else:
			raise TypeError("Invalid inventory value: %s" % value)