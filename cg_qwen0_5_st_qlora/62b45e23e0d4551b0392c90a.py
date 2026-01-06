def validate_version_inventories(self, version_dirs):
	"""
	Each version SHOULD have an inventory up to that point.

Also keep a record of any content digests different from those in the root inventory
so that we can also check them when validating the content.
	"""
	for vdir in version_dirs:
		v = self.get_version(vdir)
		if not v:
			raise InvalidVersionError("No such version: %s" % vdir)

		# Check for content digests
		content_digests = set()
		for f in os.listdir(v.dir):
			if f.startswith("."):
				continue
			f = os.path.join(v.dir, f)
			with open(f) as fh:
				content_digests.add(hashlib.sha1(fh.read()).hexdigest())
		for d in self.root_inventory.digests:
			if d not in content_digests:
				raise InvalidContentDigestError("Invalid content digest: %s" % d)