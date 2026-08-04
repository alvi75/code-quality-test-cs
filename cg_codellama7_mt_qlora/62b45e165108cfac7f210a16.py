def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if self.version != prior.version:
		return self.error("Inventory version mismatch: %s != %s" % (self.version, prior.version))
	if self.name != prior.name:
		return self.error("Inventory name mismatch: %s != %s" % (self.name, prior.name))
	if self.description != prior.description:
		return self.error("Inventory description mismatch: %s != %s" % (self.description, prior.description))
	if self.version_date != prior.version_date:
		return self.error("Inventory version date mismatch: %s != %s" % (self.version_date, prior.version_date))
	if self.version_number != prior.version_number:
		return self.error("Inventory version number mismatch: %s != %s" % (self.version_number, prior.version_number))
	if self.version_string != prior.version_string:
		return self.error("Inventory version string mismatch: %s != %s" % (self.version_string, prior.version_string))
	if self.version_string_short != prior.version_string_short:
		return self.error("Inventory version string short mismatch: %s != %s" % (self.version_string_short, prior.version_string_short))
	if self.version_string_long != prior.version_string_long:
		return self.error("Inventory version string long mismatch: %s != %s" % (self.version_string_long, prior.version_string_long))
	if self.version_string_long_short != prior.version_string_long_short:
		return self.error("Inventory version string long short mismatch: %s != %s" % (self.version_