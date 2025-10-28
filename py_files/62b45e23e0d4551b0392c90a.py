def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	if not self.root_inventory:
		return

	for vdir in version_dirs:
		v = Version(vdir)
		inventory_path = os.path.join(self.inventory_dir, v.name + '.json')
		try:
			with open(inventory_path) as f:
				inventory = json.load(f)
		except IOError:
			raise InventoryError('Inventory file %s does not exist' % inventory_path)

		self.validate_inventory(inventory, v)