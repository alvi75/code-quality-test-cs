def build_app_logger(name='app', logfile='app.log', debug=True):
		"""
		General purpose application logger. Useful mainly for debugging
    Args:
        name: The name of logger
        logfile: The log file need to save
        debug: is need to debug

    Returns:
        Returns an instantiated logger object
	"""
	# Create a basic config
	config = {
		'version': 1,
		'disable_existing_loggers': False,
		'formatters': {
			'basic': {
				'format': '%(name)s %(levelname)-8s %(message)s'
			}
		},
		'handlers': {
			'console': {
				'level': 'DEBUG',
				'class': 'logging.StreamHandler',
				'formatter': 'basic'
			}
		},
		'loggers': {
			'app': {
				'handlers': ['console'],
				'level': 'DEBUG',
				'propagate': False,
				'no_colors': True
			}
		}
	}

	if debug:
		logging.basicConfig(
			level=logging.DEBUG,
			format='%(name)s %(levelname)-8s %(message)s'
		)

	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)

	# Add handlers
	for handler in logger.handlers:
		logger.removeHandler(handler)

	# Set up console handler
	console_handler = logging.StreamHandler()
	console_handler.setLevel('DEBUG')
	console_handler.setFormatter(logging.Formatter('%(name)s %(levelname)-8s %(message)s'))
	logger.addHandler(console_handler)

	# Setup file handler if needed
	if os.path.isfile(logfile) and not os.path.getsize(logfile):
		file_handler = logging.FileHandler(logfile, mode='a+')
		file_handler.setLevel('INFO')
		file_handler.setFormatter(logging.Formatter('%(name)s %(levelname)-8s %(message)s'))
		logger.addHandler(file_handler)

	return logger