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
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Set formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(logfile)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if debug:
        logger.debug('Debug mode enabled')

    return logger