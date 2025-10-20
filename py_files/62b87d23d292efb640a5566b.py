def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, str):
		commands = [commands]
	for cmd in commands:
		cmd = shlex.split(cmd)
		args.extend(cmd)

	return _run(args, cwd=cwd, verbose=verbose, hide_stderr=hide_stderr, env=env)