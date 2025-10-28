def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.
	"""
	for vdir in version_dirs:
		vname = self._get_vname(vdir)
		if not os.path.exists(vdir):
			self.log.error("Version directory %s does not exist", vdir)
			continue

		# Check if the version directory contains an inventory file
		inventory_file = os.path.join(vdir, "inventory")
		if not os.path.isfile(inventory_file):
			self.log.error("Version directory %s does not contain an inventory file", vdir)
			continue

		# Check if the version directory contains an inventory digest file
		digest_file = os.path.join(vdir, "digest")
		if not os.path.isfile(digest_file):
			self.log.error("Version directory %s does not contain an inventory digest file", vdir)
			continue

		# Check if the version directory contains an inventory digest digest
		digest = self.get_inventory_digest(vdir)
		if not digest:
			self.log.error("Version directory %s does not contain an inventory digest", vdir)
			continue

		# Check if the version directory contains an inventory digest digest
		if digest != self.get_inventory_digest(vdir):
			self.log.warning("Version directory %s has an inventory digest but it does not match the one in the root inventory",
			                  vdir)

		# Check if the version directory contains an inventory digest digest
		if digest == self.get_inventory_digest(vdir):
			self.log.debug("Version directory %s has an inventory digest digest", vdir)