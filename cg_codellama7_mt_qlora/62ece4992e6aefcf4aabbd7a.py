def is_gitbash():
	"""
	Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
	"""
	if os.name == 'nt':
		if os.environ.get('MSYSTEM', '').startswith('MINGW'):
			return True
		elif os.environ.get('TERM', '').startswith('xterm'):
			return True
	return False