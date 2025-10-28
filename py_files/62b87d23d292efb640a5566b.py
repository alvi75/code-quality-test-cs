def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, (list, tuple)):
		raise TypeError("commands must be a list or tuple")
	if not isinstance(args, (list, tuple)):
		args = [args]
	cmds = []
	for cmd in commands:
		cmds.append(cmd.format(*args))
	if verbose:
		print(' '.join(cmds), file=sys.stderr)
	return subprocess.check_call(cmds, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)