def is_gitbash():
	"""
	Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
	"""
	if os.name == 'nt':
		return os.environ.get('COMSPEC') == r'"{0}\comspec"'.format(os.path.dirname(sys.executable))
	else:
		return False