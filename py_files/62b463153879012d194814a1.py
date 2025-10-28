def add_rendition(self, lang, file_path):
	"""
	Assign the filepath invoke by filepath() in the class to "lang" in _renditions in the class.
	"""
	if not self._renditions:
		self._renditions = {}
	for key in self._renditions.keys():
		if key == lang:
			raise Exception("The language '%s' is already assigned." % lang)
	self._renditions[lang] = file_path