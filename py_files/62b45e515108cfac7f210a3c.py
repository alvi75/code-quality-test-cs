def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if self.root.exists():
		raise FileExistsError(f"Storage root {self.root} already exists")
	self.root.mkdir()
	self._initialize_root()