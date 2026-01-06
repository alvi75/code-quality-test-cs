def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, list):
		commands = [commands]

	for cmd in commands:
		cmd = cmd.split()
		cmd.extend(args)
		if verbose:
			print("Running: %s" % " ".join(cmd))
		try:
			subprocess.check_call(cmd, cwd=cwd, env=env)
		except subprocess.CalledProcessError as e:
			if hide_stderr:
				print(e.output)
			else:
				raise e