def load_configurations(config_filenames, overrides=None, resolve_env=True):
	"""
	Given a sequence of configuration filenames, load and validate each configuration file. If the configuration file
	cannot be read due to insufficient permissions or error parsing configuration file, the error log will
	be recorded. Otherwise, return the results as a tuple of: dict of configuration filename to corresponding parsed configuration,
	and sequence of logging.LogRecord instances containing any parse errors.
	"""
	configs = {}
	for config_filename in config_filenames:
		if not os.path.exists(config_filename):
			raise ValueError("Configuration file %r does not exist." % config_filename)
		try:
			with open(config_filename) as f:
				config = ConfigParser.SafeConfigParser()
				config.readfp(f)
				configs[config_filename] = config
		except Exception as e:
			log_record = LogRecord(
				level=logging.ERROR,
				filename=config_filename,
				message="Error loading configuration file %r: %s" % (config_filename, str(e)),
				stack_info=True,
			)
			yield log_record
			continue

		if overrides is None:
			overrides = {}

		for section_name, section in config.items():
			if section_name not in overrides:
				continue
			for option_name, value in overrides[section_name].items():
				if option_name not in section:
					raise ValueError("Configuration file %r has no option %r for section %r" % (config_filename, option_name, section_name))
				if value is None:
					value = ""
				elif isinstance(value, bool):
					value = "true" if value else "false"
				elif isinstance(value, int):
					value = str(value)
				elif isinstance(value, float):
					value = str(value)
				else:
					raise TypeError("Unsupported type for option %r in section %r: %r" % (option_name, section_name, value))

				if section_name == "environment":
					env_var = "%s_%s" % (section_name, option_name)
					if env_var in os.environ:
						value = os.environ[env_var]
				elif section_name == "log":
					if option_name == "level":
						value = getattr(logging, value.upper())
					elif option_name == "format":
						value = value.replace("%(asctime)s", "[%H:%M]")
				elif section_name == "debug":
					if option_name == "format":
						value = "[DEBUG] %(message)s"

				if value is