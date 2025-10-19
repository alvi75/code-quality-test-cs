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
	logger = logging.getLogger(name)
	if len(logger.handlers) > 0:
		for handler in logger.handlers:
			logger.removeHandler(handler)

	level = logging.DEBUG if debug else logging.INFO
	logging_format = '%(asctime)s - [%(levelname)s] - %(message)s'
	logging.basicConfig(level=level, format=logging_format,
						filename=logfile, filemode='w')
	return logger