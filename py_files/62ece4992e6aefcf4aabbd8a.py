def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. If the configuration file
	cannot be read due to insufficient permissions or error parsing configuration file, the error log will
	be recorded. Otherwise, return the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
	and sequence of logging.LogRecord instances containing any parse errors.
	"""
	config = {}
	for config_filename in config_filenames:
		if not os.path.exists(config_filename):
			raise ValueError("Configuration file %s does not exist" % config_filename)
		try:
			with open(config_filename) as f:
				config[config_filename] = yaml.safe_load(f)
		except Exception as e:
			log.error("Error loading configuration file %s: %s", config_filename, str(e))
			continue

	# Resolve environment variables if requested
	if resolve_env:
		for key in config.keys():
			if isinstance(config[key], six.string_types):
				config[key] = os.environ.get(key)

	# Validate configuration
	errors = []
	for key in config.keys():
		if isinstance(config[key], dict):
			for subkey in config[key].keys():
				if not isinstance(config[key][subkey], six.string_types):
					errors.append(LogRecord(
						"Invalid configuration value for key '%s' in file '%s': %s" % (subkey, config_filename, config[key][subkey]),
						1000, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None