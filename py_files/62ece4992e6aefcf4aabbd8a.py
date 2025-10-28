def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. If the configuration file
cannot be read due to insufficient permissions or error parsing configuration file, the error log will
be recorded. Otherwise, return the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
and sequence of logging.LogRecord instances containing any parse errors.
	"""
	configs = {}
	errors = []
	for config_filename in config_filenames:
		try:
			if not os.path.isfile(config_filename):
				raise IOError("Configuration file %r does not exist" % (config_filename,))
			config = ConfigParser()
			config.read(config_filename)
			if resolve_env:
				resolve_environment_variables(config)
			configs[config_filename] = config
		except Exception as e:
			errors.append(logging.LogRecord(None, None, 'ERROR', None, "Error loading configuration file '%s': %s" % (config_filename, str(e)), 0, None))
	return configs, errors