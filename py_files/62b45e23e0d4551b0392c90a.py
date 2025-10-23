def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	for version_dir in version_dirs:
		if not os.path.exists(os.path.join(self.root_dir, version_dir)):
			raise Exception("Version %s does not exist" % version_dir)
		inventory_path = os.path.join(self.root_dir, version_dir, 'inventory')
		if not os.path.exists(inventory_path):
			raise Exception("Version %s has no inventory file" % version_dir)

		with open(inventory_path) as f:
			inventory = json.load(f)

		for key in inventory.keys():
			if key == 'content':
				continue

			if key not in self.root_inventory:
				raise Exception("Version %s has an unknown key: %s" % (version_dir, key))

			if self.root_inventory[key] != inventory[key]:
				raise Exception("Version %s has a different value for %s than the root inventory" % (version_dir, key))