def add_asset(self, basename, file_path):
	"""
	Assign the filepath invoke by filepath() in the class to "basename" in _assets in the class.
	"""
	if basename in self._assets:
		raise ValueError("Asset with name %s already exists" % basename)
	self._assets[basename] = file_path