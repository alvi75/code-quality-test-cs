def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, (list, tuple)):
		commands = [commands]
	if not isinstance(args, (list, tuple)):
		args = [args]

	cmds = []
	for cmd in commands:
		cmds.append(cmd)
	if verbose:
		print("Running: %s" % " ".join(cmds))
	try:
		return subprocess.check_call(cmds, cwd=cwd, env=env, stdout=subprocess.PIPE,
		                                stderr=subprocess.PIPE if hide_stderr else None)
	except subprocess.CalledProcessError as e:
		if hide_stderr:
			sys.stderr.write(e.output)
		else:
			sys.stderr.write(str(e))