def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not cmd:
		return cmd
	if os.path.isabs(cmd[0]):
		return cmd
	if os.path.isabs(os.path.dirname(cmd[0])):
		return cmd
	return (os.path.join(os.getcwd(), cmd[0]),) + cmd[1:]