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
			log.error("Configuration file %s does not exist", config_filename)
			continue

		try:
			with open(config_filename) as f:
				config.update(yaml.safe_load(f))
		except Exception as e:
			log.error("Error loading configuration file %s: %s", config_filename, str(e))

		if overrides is None:
			overrides = {}

		for key, value in overrides.items():
			if key in config:
				if isinstance(value, dict):
					config[key] = merge_dicts(config[key], value)
				else:
					config[key] = value

		if resolve_env:
			for key, value in config.items():
				if isinstance(value, dict):
					for k, v in value.items():
						if k.startswith('env_'):
							env_key = k[len('env_'):]
							if env_key in os.environ:
								value[k] = os.environ[env_key]
				elif k.startswith('env_'):
					env_key = k[len('env_'):]
					if env_key in os.environ:
						value = os.environ[env_key]

		return config, [logging.log_record()]