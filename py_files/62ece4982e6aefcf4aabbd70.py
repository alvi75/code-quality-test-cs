def os_is_mac():
		"""
		Checks if the os is macOS

    :return: bool, True is macOS, otherwise False.
		"""
		if sys.platform == 'darwin':
			return True
		else:
			return False
	os_is_mac = os_is_mac
	return os_is_mac