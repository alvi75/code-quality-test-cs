def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	return cmd if isinstance(cmd, str) else (os.path.abspath(os.path.expandvars(cmd)), )