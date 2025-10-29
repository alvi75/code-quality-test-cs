def get_versions():
	"""
	Obtains the version information. If the version information cannot be obtained, the default value is returned.
	"""
	try:
		with open(os.path.join(os.path.dirname(__file__), 'version.py')) as f:
			version = f.read()
	except IOError:
		return DEFAULT_VERSION
	else:
		exec(version, globals(), locals())
		return locals()['__version__']