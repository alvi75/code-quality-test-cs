def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if self._initialized:
		raise RuntimeError("Storage already initialized")
	self._initialized = True
	self._root = OCFLRoot(self, None)