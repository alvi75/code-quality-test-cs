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
			config = load_configuration(config_filename, overrides=overrides, resolve_env=resolve_env)
			configs[config_filename] = config
		except Exception as e:
			errors.append(logging.LogRecord(
				name='config',
				level=logging.ERROR,
				msg=str(e),
				args=(),
				exc_info=sys.exc_info(),
				stack_info=True,
				timestamp=time.time()
			))
	return configs, errors