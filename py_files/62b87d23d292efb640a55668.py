def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	config._version = __version__
	config._git_tag = __git_tag__
	config._git_branch = __git_branch__
	config._git_hash = __git_hash__
	return config