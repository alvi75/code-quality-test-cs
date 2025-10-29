def is_gitbash():
	"""
	Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
	"""
	if sys.platform == 'win32':
		return os.environ.get('MSYS') or os.environ.get('MINGW_PREFIX')
	else:
		return False