def normalize_cmd(cmd: tuple[str, ...]) -> tuple[str, ...]:
	"""
	Complement the full path to exe and return it in its original form
	"""
	if not cmd:
		return ()
	exe = os.path.basename(cmd[0])
	if not exe or not os.path.isfile(exe):
		return cmd
	for i, arg in enumerate(cmd):
		if arg == exe:
			cmd[i] = os.path.abspath(exe)
	return cmd