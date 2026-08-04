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
	logger.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	if debug:
		handler = logging.StreamHandler()
		handler.setLevel(logging.DEBUG)
		handler.setFormatter(formatter)
		logger.addHandler(handler)
	handler = logging.FileHandler(logfile)
	handler.setLevel(logging.INFO)
	handler.setFormatter(formatter)
	logger.addHandler(handler)
	return logger