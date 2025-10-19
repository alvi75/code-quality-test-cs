def os_is_mac():
	"""
	Checks if the os is macOS

    :return: bool, True is macOS, otherwise False.
	"""
	if sys.platform.startswith('darwin') \
		or 'darwin' in sys.platform.lower() \
		or platform.mac_ver()[0] != '':
		return True
	else:
		return False