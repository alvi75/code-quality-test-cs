def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if len(cmd) == 1:
		return cmd[0], cmd[0]
	else:
		return cmd[0], os.path.join(os.getcwd(), cmd[0])