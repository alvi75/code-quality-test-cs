def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config.version = '0.0.0'
	config.branch = 'master'
	config.dist = 'sdist'
	config.tag_format = '{version}-{commit}{branch}'
	config.template_dir = os.path.join(os.path.dirname(__file__), 'templates')
	return config