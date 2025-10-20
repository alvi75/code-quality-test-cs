def validate(self, inventory, extract_spec_version=False):
	"""
	Validate a given inventory. If extract_spec_version is True then will look at the type value to determine the specification version. In the case that there is no type value or it isn't valid, then other tests will be based on the version given in self.spec_version. (D)
	"""
	if not isinstance(inventory, dict):
		raise ValueError("Inventory must be a dictionary.")
	for key in inventory:
		if key == "type":
			continue
		elif key in self._valid_keys:
			pass
		else:
			raise KeyError("Invalid key: %s" % key)

	if extract_spec_version:
		try:
			spec_version = inventory["type"]
		except KeyError:
			spec_version = self.spec_version

		if spec_version not in self.valid_versions:
			raise ValueError("Unknown specification version: %s" % spec_version)