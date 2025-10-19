def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if len(cmd) < 2:
		return cmd

	exe = os.path.join(os.path.dirname(cmd[0]), cmd[1])
	return (exe,) + cmd[2:]