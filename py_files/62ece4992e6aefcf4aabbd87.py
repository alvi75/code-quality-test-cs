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

	if not os.path.exists(logfile):
	    with open(logfile, 'w') as f:
	        pass

	handler = logging.StreamHandler()
	handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	logger.addHandler(handler)

	if debug:
	    handler.setLevel(logging.DEBUG)

	return logger