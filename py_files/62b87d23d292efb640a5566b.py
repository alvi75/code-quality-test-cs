def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, list):
		commands = [commands]
	for cmd in commands:
		cmd_args = [cmd] + args
		if verbose:
			print("Running: %s" % " ".join(cmd_args))
		try:
			subprocess.check_call(cmd_args, cwd=cwd, env=env)
		except subprocess.CalledProcessError as e:
			if hide_stderr:
				print("ERROR: %s" % e)
			else:
				print("ERROR: %s\n%s" % (e, e.output))