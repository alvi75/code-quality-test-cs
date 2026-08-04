def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if self.storage_root.exists():
		raise OCFLObjectException("Storage root already exists")
	self.storage_root.mkdir(parents=True)
	self.storage_root.joinpath('config.json').write_text(json.dumps(self.config))