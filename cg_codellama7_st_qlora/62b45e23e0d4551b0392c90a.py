def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.

version_dirs is an array of version directory names and is assumed to be in
version sequence (1, 2, 3...).
	"""
	root_inventory = self.inventory
	root_content_digests = root_inventory.get_content_digests()
	for version_dir in version_dirs:
		version_inventory = self.get_inventory(version_dir)
		version_content_digests = version_inventory.get_content_digests()
		for content_digest in version_content_digests:
			if content_digest not in root_content_digests:
				raise ValidationError("Version inventory %s contains content digest %s not in root inventory" % (version_dir, content_digest))
			if version_content_digests[content_digest] != root_content_digests[content_digest]:
				self.different_content_digests[content_digest] = (version_content_digests[content_digest], root_content_digests[content_digest])