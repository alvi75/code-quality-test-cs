def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list):
		raise TypeError("commands must be a list")
	for cmd in commands:
		if not isinstance(cmd, str):
			raise TypeError("each element in commands must be a string")

	if not isinstance(args, list):
		args = [args]
	
	cmds = []
	for c in commands:
		cmds.append(c + " " + " ".join(args))
	
	if verbose:
		print("\n".join(cmds))

	p = Popen(cmds, stdout=PIPE, stderr=STDOUT if not hide_stderr else PIPE, cwd=cwd, shell=True, env=env)

	try:
		out, err = p.communicate()
	except KeyboardInterrupt as e:
		p.kill()
		raise e

	return p.returncode, out, err