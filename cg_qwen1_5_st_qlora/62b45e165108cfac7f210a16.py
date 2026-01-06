def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if not isinstance(prior, InventoryValidator):
		raise TypeError("prior must be an instance of InventoryValidator")
	if prior.inventory_type != self.inventory_type:
		return "Inventory type mismatch"
	if prior.version < self.version:
		return "Prior version (%s) is less than current version (%s)" % (prior.version, self.version)
	if prior.version > self.version:
		return "Prior version (%s) is greater than current version (%s)" % (prior.version, self.version)
	for key in prior.keys():
		if key not in self.keys():
			return "Key '%s' missing from current inventory" % key
		if prior[key] != self[key]:
			return "Key '%s' differs between current and prior inventory" % key
	return None