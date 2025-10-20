def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	root_inventory = self.get_root_inventory()
	for version_dir_name in version_dirs:
		version_dir_path = os.path.join(self.root_dir, version_dir_name)
		inventory_file_path = os.path.join(version_dir_path, 'inventory')
		if not os.path.exists(inventory_file_path):
			raise InventoryError('No inventory file found for %s' % version_dir_name)

		with open(os.path.join(version_dir_path, 'inventory')) as f:
			content_digests = {}
			for line in f.readlines():
				line = line.strip().split('\t', 1)
				if len(line) != 2:
					continue

				digest, path = line
				content_digests[path] = digest

		try:
			self.validate_content_digests(content_digests, version_dir_path)
		except ContentDigestMismatchError as e:
			e.version_dir_name = version_dir_name
			raise

		root_inventory.add_version(version_dir_name, version_dir_path)