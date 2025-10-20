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
			if not os.path.isfile(config_filename) or not os.access(config_filename, os.R_OK):
				raise IOError("Cannot open configuration file '%s' for reading" % (config_filename,))
			config = ConfigParser()
			config.readfp(open(config_filename))
			if overrides is not None:
				config.setdefaults(overrides)
			configs[config_filename] = config
		except Exception as e:
			err_msg = "Error loading configuration file '%s': %s" % (config_filename, str(e))
			logger.error(err_msg)
			errors.append(logging.LogRecord('error', logging.ERROR, 'load-config', 0, err_msg, [], None))

	return configs, errors