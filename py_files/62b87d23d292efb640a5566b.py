def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, (list, tuple)):
		commands = [commands]
	
	for cmd in commands:
		cmd = shlex.split(cmd)
		
		if verbose:
			print("Running: %s" % " ".join(cmd))
		
		try:
			subprocess.check_output(cmd + args, cwd=cwd, stderr=subprocess.STDOUT if hide_stderr else subprocess.PIPE, env=env)
		except subprocess.CalledProcessError as e:
			raise CommandException(e.output.decode('utf-8'))