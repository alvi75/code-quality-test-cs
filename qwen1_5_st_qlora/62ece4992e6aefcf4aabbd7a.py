def is_gitbash():
	"""
	Check whether the current program is run in a Windows gitbash terminal

    Returns:
            boolean, True if gitbash else False
	"""

	if os.name == 'nt':
		pattern = re.compile(r'git-bash')
	else:
		return False

	for line in subprocess.check_output(['cmd', '/c', 'echo %windir%']).splitlines():
		line = line.decode('utf-8').strip()
		if pattern.search(line):
			return True

	return False