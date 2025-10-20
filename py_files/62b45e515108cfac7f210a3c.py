def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if self._root is not None:
		raise RuntimeError("Storage root already initialized")
	self._root = OCFLStorageRoot(self, self._storage)
	self._root.initialize()