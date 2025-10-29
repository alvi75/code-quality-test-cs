def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	for version_dir in version_dirs:
		if not os.path.exists(os.path.join(self.root_path, version_dir)):
			raise Exception("Version %s does not exist" % version_dir)
		inventory = self.get_inventory(version_dir)
		if not inventory:
			raise Exception("No inventory found for version %s" % version_dir)

		# Check that all the files in the inventory are present.
		for filename in inventory.files:
			if not os.path.exists(os.path.join(self.root_path, version_dir, filename)):
				raise Exception("File %s missing from version %s" % (filename, version_dir))

		# Check that all the directories in the inventory are present.
		for dirname in inventory.directories:
			if not os.path.exists(os.path.join(self.root_path, version_dir, dirname)):
				raise Exception("Directory %s missing from version %s" % (dirname, version_dir))