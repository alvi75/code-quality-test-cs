def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	if config.versionfile_source is None:
		config.versionfile_source = 'setup.py'
	if config.versionfile_template is None:
		config.versionfile_template = 'VERSION'
	if config.full_version is False:
		config.full_version = True
	return config