def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if len(cmd) == 1:
		return cmd
	for i, arg in enumerate(cmd):
		if os.path.isfile(arg):
			cmd[i] = os.path.abspath(arg)
	return cmd