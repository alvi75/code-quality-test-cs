def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list):
		commands = [commands]

	for cmd in commands:
		if not isinstance(cmd, list):
			cmd = [cmd]
		if not isinstance(args, list):
			args = [args]
		cmd.extend(args)

	if verbose:
		print("Running command: %s" % " ".join(cmd))

	p = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=cwd, env=env)
	stdout, stderr = p.communicate()
	returncode = p.returncode

	if hide_stderr:
		stderr = ""

	if verbose:
		print("Command output:")
		print(stdout.decode('utf-8'))
		print(stderr.decode('utf-8'))

	return stdout, stderr, returncode