def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if len(cmd) == 1:
		return cmd

	exe = cmd[0]
	if not os.path.isabs(exe):
		exe = os.path.abspath(exe)

	return (exe,) + tuple(cmd[1:])