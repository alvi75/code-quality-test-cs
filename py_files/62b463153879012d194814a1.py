def add_rendition(self, lang, file_path):
	"""
	Assign the filepath invoke by filepath() in the class to "lang" in _renditions in the class.
	"""
	self._renditions[lang] = file_path