def os_is_mac():
	"""
	Checks if the os is macOS

    :return: bool, True is macOS, otherwise False.
	"""
	return sys.platform.startswith('darwin') or \
			'__MACOSX__' in os.environ.get('__COMPILER_GNU__', '')