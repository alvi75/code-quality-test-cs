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
		file_handler = logging.FileHandler(logfile, 'a')
		file_handler.setLevel(logging.DEBUG)
		file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		file_handler.setFormatter(file_formatter)
		logger.addHandler(file_handler)

	if debug:
		stream_handler = logging.StreamHandler()
		stream_handler.setLevel(logging.DEBUG)
		stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		stream_handler.setFormatter(stream_formatter)
		logger.addHandler(stream_handler)

	return logger