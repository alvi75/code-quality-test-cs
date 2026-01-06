def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	self._storage_root = StorageRoot()
	self._storage_root.initialize()