def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if not isinstance(prior, InventoryValidator): return error("prior must be an InventoryValidator object")
	for k in self:
		if not (k in prior or k == "version"): # allow extra keys in the newer version
			return error("%s: missing from prior" % k)
		elif not self[k].validate_as_prior_version(prior[k]): return error("%s: mismatch" % k)