def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""

	try:
		return __get_version_info()
	except Exception as e:
		print("Failed to obtain version information: %s" % str(e))
		return "unknown"