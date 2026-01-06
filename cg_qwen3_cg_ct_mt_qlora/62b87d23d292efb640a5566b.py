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
		if env is None:
			env = os.environ.copy()
		else:
			env.update(os.environ)

		try:
			subprocess.check_call(cmd, cwd=cwd, stderr=subprocess.DEVNULL if hide_stderr else None, env=env)
		except subprocess.CalledProcessError as e:
			raise CommandFailed(e)