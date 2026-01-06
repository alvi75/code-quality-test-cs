def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, list):
		commands = [commands]
	if not isinstance(args, list):
		args = [args]

	for cmd in commands:
		run_command_with_args(cmd, args, cwd=cwd, verbose=verbose, hide_stderr=hide_stderr, env=env)