def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list):
		raise ValueError("commands must be a list")
	if not isinstance(args, list):
		raise ValueError("args must be a list")

	cmds = []
	for cmd in commands:
		cmds.append(cmd + " " + args)

	return run_commands(cmds, cwd=cwd, verbose=verbose, hide_stderr=hide_stderr, env=env)