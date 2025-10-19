def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. If the configuration file
cannot be read due to insufficient permissions or error parsing configuration file, the error log will
be recorded. Otherwise, return the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
and sequence of logging.LogRecord instances containing any parse errors.
	"""
	configs = {}
	for config_filename in config_filenames:
		try:
			with open(config_filename) as f:
				config = configparser.ConfigParser()
				config.readfp(f)
				configs[config_filename] = _load_and_validate_config(config, config_filename, overrides=overrides, resolve_env=resolve_env)
		except (OSError, PermissionError) as e:
			logging.error("Failed to read configuration file %r", config_filename)
			logging.exception(e)
			continue

	return configs, []