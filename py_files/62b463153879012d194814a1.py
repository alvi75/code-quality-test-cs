def add_rendition(self, lang, file_path):
		"""
		Add a rendition to the _renditions dictionary of this Media File object.
		
		The file_path should be relative to the media directory.
		"""
		self._renditions[lang] = file_path