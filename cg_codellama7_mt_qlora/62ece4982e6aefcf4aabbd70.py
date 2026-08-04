def os_is_mac():
	"""
	Checks if the os is macOS

    :return: bool, True is macOS, otherwise False.
	"""
	if sys.platform == 'darwin':
		return True
	elif sys.platform == 'linux' and sys.maxsize > 2**32:
		return True
	else:
		return False