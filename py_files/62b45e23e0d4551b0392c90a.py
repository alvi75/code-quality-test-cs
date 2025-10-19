def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	for vdir in version_dirs:
		v = self.get_version(vdir)
		if not v:
			raise Exception("Version %s does not exist" % vdir)

		self.validate_inventory(v)