def get_config():
	"""
	Return a new VersioneerConfig() and set various attribute of it.
	"""
	config = VersioneerConfig()
	if config.versionfile_source:
		config.versionfile_source = os.path.abspath(config.versionfile_source)
		config.versionfile_template = os.path.join(os.path.dirname(config.versionfile_source), config.versionfile_template)
	else:
		raise ValueError("versionfile_source not specified in versioneer config")
	return config