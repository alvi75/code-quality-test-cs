def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	if 'VCS' in config.versionfile_source:
		raise ValueError(
			"VCS specified without versionfile_source, "
			"you probably need to specify versionfile_source"
		)
	if not config.tag_prefix:
		config.tag_prefix = "v"
	if not config.verbose:
		config.verbose = 0
	if not config.no_vcs:
		config.no_vcs = False
	return config