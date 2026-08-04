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
		print("Running command:", commands, args)
	if hide_stderr:
		stderr = subprocess.PIPE
	else:
		stderr = None
	if env is None:
		env = os.environ
	try:
		p = subprocess.Popen(commands + args, cwd=cwd, env=env, stderr=stderr)
	except OSError as e:
		if e.errno == errno.ENOENT:
			raise CommandNotFoundError(commands[0])
		else:
			raise
	if hide_stderr:
		_, stderr = p.communicate()
		if stderr:
			print(stderr.decode("utf-8"), file=sys.stderr)
	return p.returncode