def build_app_logger(name='app', logfile='app.log', debug=True):
		"""
		def build_app_logger(name='app', logfile='app.log', debug=True):
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

	# create a console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	if debug:
	    ch.setLevel(logging.DEBUG)
	else:
	    ch.setLevel(logging.INFO)
	# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	formatter = logging.Formatter(
		'%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(funcName)s:%(lineno)d - %(message)s'
	)
	ch.setFormatter(formatter)

	# add the handlers to the logger
	logger.addHandler(ch)

	# create a file handler and set a specific log level
	fh = logging.FileHandler(logfile, 'w')
	fh.setLevel(logging.DEBUG)
	fh.setFormatter(formatter)

	# add the handlers to the logger
	logger.addHandler(fh)

	return logger