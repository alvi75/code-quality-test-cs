def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	for version_dir in version_dirs:
		version = self.get_version(version_dir)
		if not version:
			continue

		# Check that the version has an inventory
		if not version.inventory:
			self.log.error("Version %s does not have an inventory", version_dir)
			continue

		# Check that the version has a root inventory
		if not version.root_inventory:
			self.log.error("Version %s does not have a root inventory", version_dir)
			continue

		# Check that the version has a digest for each file
		for filename in os.listdir(version.root_inventory):
			digest = version.root_inventory[filename]
			if digest == "":
				self.log.error("Version %s has no digest for %s", version_dir, filename)
				continue

			# Check that the digest matches the digest of the file
			if digest != hashlib.md5(open(os.path.join(version.root_inventory, filename), "rb").read()).hexdigest():
				self.log.error("Version %s has a digest mismatch for %s", version_dir, filename)