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
	if not hasattr(logger, 'handlers'):
		logger.setLevel(logging.DEBUG if debug else logging.INFO)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	hdlr = logging.StreamHandler()
	hdlr.setFormatter(formatter)
	hdlr.setLevel(logging.DEBUG)
	hdlr.addFilter(logging.Filter('app'))
	logger.addHandler(hdlr)

	return logger