def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not isinstance(cmd, tuple):
		cmd = (cmd,)
	return os.path.normpath(os.path.join(*cmd))