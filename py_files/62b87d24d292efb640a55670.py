def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		return __get_version()
	except Exception as e:
		return "Unknown"