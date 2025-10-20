def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if not isinstance(prior, InventoryValidator):
		self.error("prior must be an instance of InventoryValidator")
	if not self.is_valid():
		return
	if not prior.is_valid():
		self.error("prior must be a valid prior version of the current inventory object")