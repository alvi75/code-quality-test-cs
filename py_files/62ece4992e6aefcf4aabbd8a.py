def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. If the configuration file
	cannot be read due to insufficient permissions or error parsing configuration file, the error log will
	be recorded. Otherwise, return the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
	and sequence of logging.LogRecord instances containing any parse errors.
	"""
	config = {}
	for config_filename in config_filenames:
		if not os.path.isfile(config_filename):
			log.error("Configuration file %s does not exist", config_filename)
			continue

		try:
			with open(config_filename) as f:
				config.update(yaml.load(f))
		except Exception as e:
			log.error("Error loading configuration file %s: %s", config_filename, e)

		if overrides is not None:
			config.update(overrides)

		if resolve_env:
			resolve_env = False

		return config, _parse_errors(config)