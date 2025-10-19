def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	self._root = self._make_root()
	self._root.initialize()