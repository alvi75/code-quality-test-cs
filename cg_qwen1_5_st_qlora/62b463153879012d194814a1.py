def add_rendition(self, lang, file_path):
	"""
	Assign the filepath invoke by filepath() in the class to "lang" in _renditions in the class.
	"""
	if not self._renditions:
		self._renditions = {}
	if not isinstance(lang, str):
		raise TypeError("lang must be a string")
	if not isinstance(file_path, str):
		raise TypeError("file_path must be a string")

	self._renditions[lang] = file_path