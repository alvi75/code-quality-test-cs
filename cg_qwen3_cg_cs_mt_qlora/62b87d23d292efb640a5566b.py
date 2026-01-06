def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, (list, tuple)):
		commands = [commands]

	for cmd in commands:
		if verbose:
			print("Running: %s" % " ".join([cmd] + args))
		if env is None:
			env = os.environ.copy()
		else:
			env.update(os.environ)
		p = subprocess.Popen([cmd] + args,
		                     stdout=subprocess.PIPE,
		                     stderr=subprocess.PIPE if hide_stderr else None,
		                     cwd=cwd,
		                     env=env)
		stdout, stderr = p.communicate()
		if p.returncode != 0:
			raise CommandError(p.returncode, cmd, args, stdout, stderr)