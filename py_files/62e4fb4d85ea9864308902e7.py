def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if len(cmd) == 1:
		return cmd[0]
	elif len(cmd) > 2:
		cmd = (cmd[0],)
		for i in range(1, len(cmd)):
			cmd += (' ' + cmd[i],)
		return cmd
	else:
		raise ValueError('Invalid command')