def validate_version_inventories(self, version_dirs):
	"""
Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	self.log.info("Validating inventories for each version")
	for i in range(0, len(version_dirs)):
			self.validate_inventory(version_dirs[i], i+1)