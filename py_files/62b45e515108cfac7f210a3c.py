def initialize(self):
		"""
		Create and initialize a new OCFL storage root.
		"""
		if self.root is not None:
			raise RuntimeError("Storage root already initialized")
		self.root = StorageRoot()
		self.root.initialize()