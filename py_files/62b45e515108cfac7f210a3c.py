def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	if self.root.exists():
		raise ValueError("Storage root already exists: {}".format(self.root))
	self.root.mkdir(parents=True)
	self.root.joinpath('objects').mkdir()
	self.root.joinpath('versions').mkdir()
	self.root.joinpath('manifests').mkdir()
	self.root.joinpath('metadata').mkdir()
	self.root.joinpath('metadata', 'manifests').mkdir()
	self.root.joinpath('metadata', 'signatures').mkdir()
	self.root.joinpath('metadata', 'signatures', 'public_keys').mkdir()
	self.root.joinpath('metadata', 'signatures', 'private_keys').mkdir()