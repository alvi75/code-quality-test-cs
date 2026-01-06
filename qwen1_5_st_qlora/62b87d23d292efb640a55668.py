def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	if config.versionfile_source is None:
		raise ValueError("versionfile_source not specified")
	if config.versionfile_source.endswith(".py"):
		config.versionfile_source = os.path.splitext(config.versionfile_source)[0]
	if config.tagprefix is None:
		config.tagprefix = ''
	return config