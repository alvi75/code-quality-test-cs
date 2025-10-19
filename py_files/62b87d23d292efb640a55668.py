def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	global __version__, __revision__, __release__, __branch__
	global __tags__, __author__, __license__, __url__, __download_url__
	global __maintainer__, __summary__, __description__, __keywords__
	global __license_url__, __repository__, __classifiers__

	config = VersioneerConfig()
	config.__version__ = __version__
	config.__revision__ = __revision__
	config.__release__ = __release__
	config.__branch__ = __branch__
	config.__tags__ = __tags__
	config.__author__ = __author__
	config.__license__ = __license__
	config.__url__ = __url__
	config.__download_url__ = __download_url__
	config.__maintainer__ = __maintainer__
	config.__summary__ = __summary__
	config.__description__ = __description__
	config.__keywords__ = __keywords__
	config.__license_url__ = __license_url__
	config.__repository__ = __repository__
	config.__classifiers__ = __classifiers__

	return config