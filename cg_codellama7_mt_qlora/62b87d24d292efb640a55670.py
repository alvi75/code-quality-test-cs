def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		from pkg_resources import get_distribution
		return get_distribution('pygments').version
	except:
		return 'unknown'