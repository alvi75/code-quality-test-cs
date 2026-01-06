def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""

	if self.storage_root is None:
		self.storage_root = os.path.join(self.root, 'storage')
		os.makedirs(self.storage_root)

	if not os.path.exists(os.path.join(self.storage_root, 'objects')):
		os.makedirs(os.path.join(self.storage_root, 'objects'))
		os.makedirs(os.path.join(self.storage_root, 'manifests'))

	if not os.path.exists(os.path.join(self.storage_root, 'versions')):
		os.makedirs(os.path.join(self.storage_root, 'versions'))