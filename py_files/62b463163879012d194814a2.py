def add_asset(self, basename, file_path):
		"""
		Add a new asset to the assets directory of this project.
		
		The filepath will be assigned to "basename" in _assets in this project.
		"""
		if basename not in self._assets:
			self._assets[basename] = []
		self._assets[basename].append(file_path)