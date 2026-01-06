def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if not isinstance(prior, InventoryValidator):
		raise TypeError("prior must be an InventoryValidator")
	if prior.version != self.version:
		raise ValueError("prior version %s does not match current version %s" % (prior.version, self.version))
	for key in prior.keys():
		if key not in self.keys():
			self.error("%s is missing from prior inventory" % key)
		else:
			prior_item = prior[key]
			current_item = self[key]
			if not prior_item.validate_as_current(current_item):
				self.error("%s differs between prior and current inventory" % key)