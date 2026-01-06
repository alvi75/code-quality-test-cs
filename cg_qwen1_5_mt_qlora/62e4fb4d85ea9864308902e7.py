def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not cmd:
		return ()
	elif len(cmd) == 1:
		cmd = (cmd[0],)
	else:
		cmd = list(cmd)

	for i, arg in enumerate(cmd):
		if os.path.isfile(arg):
			cmd[i] = os.path.abspath(arg)

	return tuple(cmd)