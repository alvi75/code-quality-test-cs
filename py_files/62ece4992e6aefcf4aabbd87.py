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
	if not os.path.exists(os.path.dirname(logfile)):
		os.makedirs(os.path.dirname(logfile))
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG if debug else logging.INFO)

	file_handler = logging.FileHandler(logfile, 'a')
	file_handler.setFormatter(
		logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	logger.addHandler(file_handler)

	stream_handler = logging.StreamHandler()
	stream_handler.setFormatter(
		logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
	logger.addHandler(stream_handler)

	return logger