def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	# TODO: This is a bit of a hack.  We should be able to do this without
	#       having to know the version sequence.
	for version_dir in version_dirs:
		version_inventory_path = os.path.join(self.root_dir, version_dir, 'inventory.json')
		if not os.path.exists(version_inventory_path):
			raise ValidationError("Version %s does not have an inventory.json file" % version_dir)
		version_inventory = self.load_inventory(version_inventory_path)
		if not version_inventory:
			raise ValidationError("Version %s has an empty inventory.json file" % version_dir)
		if not version_inventory.get('version'):
			raise ValidationError("Version %s has an inventory.json file with no version" % version_dir)
		if version_inventory['version'] != version_dir:
			raise ValidationError("Version %s has an inventory.json file with version %s" % (version_dir, version_inventory['version']))
		if not version_inventory.get('content_digests'):
			raise ValidationError("Version %s has an inventory.json file with no content_digests" % version_dir)
		if not version_inventory.get('content_digests_root'):
			raise ValidationError("Version %s has an inventory.json file with no content_digests_root" % version_dir)
		if not version_inventory.get('content_digests_root_version'):
			raise ValidationError("Version