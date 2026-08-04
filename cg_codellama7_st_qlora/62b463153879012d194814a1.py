def add_rendition(self, lang, file_path):
	"""
	Assign the filepath invoke by filepath() in the class to "lang" in _renditions in the class.
	"""
	if lang in self._renditions:
		raise ValueError("Rendition for language %s already exists." % lang)
	self._renditions[lang] = file_path