def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		return __get_version()
	except Exception as e:
		print("Error while obtaining version information: " + str(e))
		return DEFAULT_VERSION