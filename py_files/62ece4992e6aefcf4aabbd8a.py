def _load_configuration(filename):
		try:
			with open(filename) as f:
				return json.load(f)
		except (IOError, ValueError) as e:
			raise ConfigFileParseException("Unable to parse configuration file %s" % filename, e)

	configurations = {}
	logging_log_records = []
	for config_filename in config_filenames:
		if os.path.isfile(config_filename):
			logging_log_records += _log_parse_error(config_filename, None)
		else:
			logging_log_records += _log_parse_error(config_filename, "Configuration file does not exist")
		configurations[config_filename] = _load_configuration(config_filename)

	if resolve_env:
		resolve_environ(configurations)

	return configurations, logging_log_records