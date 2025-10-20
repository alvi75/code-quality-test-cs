def os_is_mac():
	"""
	Checks if the os is macOS

    :return: bool, True is macOS, otherwise False.
	"""
	return sys.platform == 'darwin' or \
		sys.platform.startswith('darwin')