def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if isinstance(cwd, str):
		cwd = os.path.abspath(cwd)
	if isinstance(env, dict):
		env = dict(os.environ, **env)
	if verbose:
		print("Running command: %s %s" % (commands, args))
	if hide_stderr:
		stderr = subprocess.DEVNULL
	else:
		stderr = None
	if env is None:
		env = os.environ
	if isinstance(commands, list):
		for command in commands:
			if verbose:
				print("Running command: %s %s" % (command, args))
			if hide_stderr:
				stderr = subprocess.DEVNULL
			else:
				stderr = None
			if env is None:
				env = os.environ
			subprocess.check_call([command] + args, cwd=cwd, env=env, stderr=stderr)
	else:
		if verbose:
			print("Running command: %s %s" % (commands, args))
		if hide_stderr:
			stderr = subprocess.DEVNULL
		else:
			stderr = None
		if env is None:
			env = os.environ
		result = subprocess.run([commands] + args, cwd=cwd, env=env, stderr=stderr, stdout=subprocess.PIPE)
		return result.stdout.decode('utf-8'), result.returncode