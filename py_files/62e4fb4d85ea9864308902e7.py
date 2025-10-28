def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not cmd:
		return []
	cmd = [os.path.abspath(c) for c in cmd]
	for i, c in enumerate(cmd):
		if os.path.isfile(c):
			cmd[i] = os.path.realpath(c)
	return cmd