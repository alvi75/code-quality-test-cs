def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		from pkg_resources import parse_version
		version = parse_version(__version__)
	except ImportError:
		version = DEFAULT_VERSION

	return version