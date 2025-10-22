def is_gitbash():
	"""
	Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
	"""
	if os.name == 'nt':
		return 'MSYS_VERSION' in os.environ or 'MINGW_PACKAGE_NAME' in os.environ
	else:
		return False