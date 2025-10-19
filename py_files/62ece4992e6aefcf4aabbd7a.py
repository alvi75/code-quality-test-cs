def is_gitbash():
	"""
	Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
	"""
	if sys.platform.startswith('win32'):
		if 'GIT_BASH' in os.environ:
			return True
		else:
			return False
	else:
		return False