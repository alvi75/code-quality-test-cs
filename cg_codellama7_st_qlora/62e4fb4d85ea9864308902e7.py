def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not cmd:
		return cmd
	if not os.path.isabs(cmd[0]):
		cmd = (os.path.join(os.getcwd(), cmd[0]),) + cmd[1:]
	return cmd