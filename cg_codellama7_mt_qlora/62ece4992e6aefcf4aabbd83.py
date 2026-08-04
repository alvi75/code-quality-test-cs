def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if isinstance(commands, str):
		commands = [commands]
	if isinstance(args, str):
		args = [args]
	if isinstance(commands, list):
		if len(commands) == 1:
			commands = commands[0]
		else:
			commands = ' '.join(commands)
	if isinstance(args, list):
		if len(args) == 1:
			args = args[0]
		else:
			args = ' '.join(args)
	if verbose:
		print('Running command:', commands, args)
	if hide_stderr:
		stderr = subprocess.PIPE
	else:
		stderr = None
	if env is None:
		env = os.environ
	if isinstance(commands, str):
		p = subprocess.Popen(commands + ' ' + args, cwd=cwd, shell=True, stdout=subprocess.PIPE, stderr=stderr, env=env)
	else:
		p = subprocess.Popen(commands + args, cwd=cwd, stdout=subprocess.PIPE, stderr=stderr, env=env)
	stdout, stderr = p.communicate()
	return stdout, p.returncode