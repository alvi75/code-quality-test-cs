def is_gitbash():
	"""
	Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
	"""
	if os.name == 'nt':
		return sys.platform.startswith('win32') or sys.platform.startswith('cygwin')
	else:
		return False