def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		from pkg_resources import get_distribution, DistributionNotFound
		try:
			return get_distribution('pywbem').version
		except DistributionNotFound:
			return 'unknown'
	except ImportError:
		return 'unknown'