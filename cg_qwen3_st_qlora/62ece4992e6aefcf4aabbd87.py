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
	if not logger.handlers:
		handler = logging.FileHandler(logfile)
		handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
		logger.addHandler(handler)
		logger.setLevel(logging.DEBUG if debug else logging.INFO)
	return logger