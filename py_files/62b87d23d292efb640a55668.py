def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	if os.path.exists('.git'):
		config.vcs = 'git'
	else:
		raise ValueError('No .git directory found')
	return config