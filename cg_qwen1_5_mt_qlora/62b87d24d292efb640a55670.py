def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r') as f:
			version = f.read().strip()
	except IOError:
		version = "unknown"
	return version