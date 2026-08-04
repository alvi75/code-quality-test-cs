def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, basestring):
		commands = [commands]
	if isinstance(args, basestring):
		args = [args]
	if not isinstance(commands, (list, tuple)):
		raise TypeError("commands must be a list or tuple")
	if not isinstance(args, (list, tuple)):
		raise TypeError("args must be a list or tuple")
	if not commands:
		raise ValueError("commands must not be empty")
	if not args:
		raise ValueError("args must not be empty")
	if verbose:
		print("Running command: %s %s" % (commands[0], " ".join(args)))
	if hide_stderr:
		stderr = subprocess.PIPE
	else:
		stderr = None
	if env is None:
		env = os.environ
	try:
		proc = subprocess.Popen(commands + args, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=stderr)
	except OSError as e:
		if e.errno == errno.ENOENT:
			raise CommandNotFoundError("Command not found: %s" % commands[0])
		else:
			raise
	stdout, stderr = proc.communicate()
	if proc.returncode != 0:
		raise CommandError("Command failed: %s %s" % (commands[0], " ".join(args)), proc.returncode, stdout, stderr)
	return stdout