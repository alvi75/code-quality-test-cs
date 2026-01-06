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
		hdlr = RotatingFileHandler(logfile, maxBytes=1024*1024*5, backupCount=3)
		fmt = '%(asctime)s %(levelname)s %(message)s'
		datefmt='%Y-%m-%d %H:%M:%S'
		fh = logging.Formatter(fmt, datefmt=datefmt)
		hdlr.setFormatter(fh)
		logger.addHandler(hdlr)

	# set level
	if debug:
		logger.setLevel(logging.DEBUG)
	else:
		logger.setLevel(logging.INFO)

	return logger