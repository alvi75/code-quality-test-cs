def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if not self._initialized:
		self._initialize()
		self._initialized = True