def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		version = __version__
	except AttributeError:
		version = 'unknown'
	return version