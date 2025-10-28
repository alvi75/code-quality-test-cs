def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if self._initialized:
		return

	self._storage = StorageRoot(
			root=self.root,
			version=self.version,
			manifest=self.manifest,
			objects=self.objects,
			persistent_identifiers=self.persistent_identifiers,
			provenance=self.provenance,
			created_by=self.created_by,
			created_at=self.created_at,
			updated_at=self.updated_at,
			**self.storage_options)