def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if self.exists():
		raise OCFLStorageRootExistsError(
			'OCFL storage root already exists at {}'.format(self.path)
		)

	self._create_storage_root()
	self._initialize_manifests()