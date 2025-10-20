def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		with open(os.path.join(os.path.dirname(__file__), 'version.txt')) as f:
			return f.read().strip()
	except IOError:
		return DEFAULT_VERSION