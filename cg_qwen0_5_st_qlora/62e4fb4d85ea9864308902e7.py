def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not cmd:
		return None

	cmd = [os.path.abspath(c) for c in cmd]
	return tuple(cmd)