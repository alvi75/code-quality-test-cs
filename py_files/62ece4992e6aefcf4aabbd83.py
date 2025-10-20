def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list):
		commands = [commands]
	if not isinstance(args, list):
		args = [args]

	if not isinstance(cwd, str):
		cwd = os.getcwd()

	if not isinstance(env, dict):
		env = os.environ

	cmds = []
	for cmd in commands:
		cmds.append(cmd)

	return _run_cmd(cmds, args, cwd, verbose, hide_stderr, env)