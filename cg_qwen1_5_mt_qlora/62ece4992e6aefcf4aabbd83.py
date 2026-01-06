def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""

	if not isinstance(commands, list):
		raise ValueError("commands must be a list")

	if not isinstance(args, list):
		args = [args]

	cmds = []
	for cmd in commands:
		cmds.append(cmd + args)

	result = {}
	for i, cmd in enumerate(cmds):
		try:
			p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT if hide_stderr else None, shell=True, cwd=cwd, env=env)
			stdout, _stderr = p.communicate()
			result[i] = {'returncode': p.returncode, 'stdout': stdout}
		except Exception as e:
			result[i] = {'returncode': -1, 'stdout': str(e)}

	return result