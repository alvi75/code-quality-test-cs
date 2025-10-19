def initialize(self):
	"""
	Create and initialize a new OCFL storage root.
	"""
	self._storage_root = self._args.storage_root

	if os.path.exists(self._storage_root):
		raise RuntimeError("Storage root already exists: {}".format(self._storage_root))

	os.makedirs(self._storage_root)
	os.makedirs(os.path.join(self._storage_root, "blobs"))
	os.makedirs(os.path.join(self._storage_root, "blobs", "digests"))

	with open(os.path.join(self._storage_root, "blobs", "index.json"), "w") as f:
		f.write("{}")

	with open(os.path.join(self._storage_root, "blobs", "digests", "index.json"), "w") as f:
		f.write("{}")

	with open(os.path.join(self._storage_root, "metadata.json"), "w") as f:
		f.write("{}")

	with open(os.path.join(self._storage_root, "metadata", "index.json"), "w") as f:
		f.write("{}")