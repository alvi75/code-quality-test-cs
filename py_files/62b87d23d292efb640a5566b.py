def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, basestring):
		commands = [commands]
	for cmd in commands:
		cmd = shlex.split(cmd)
		run_command_inner(cmd, args, cwd=cwd, verbose=verbose, hide_stderr=hide_stderr, env=env)