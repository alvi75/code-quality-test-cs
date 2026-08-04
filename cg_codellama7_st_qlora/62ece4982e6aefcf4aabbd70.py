def os_is_mac():
    """
	Checks if the os is macOS

    :return: bool, True is macOS, otherwise False.
	"""
    if sys.platform == 'darwin':
        return True
    elif sys.platform == 'linux2':
        return False
    else:
        raise Exception('Unsupported OS: %s' % sys.platform)