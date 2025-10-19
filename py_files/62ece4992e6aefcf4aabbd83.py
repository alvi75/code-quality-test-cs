def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list): commands = [commands]
	if not isinstance(args, list): args = [args]

	for i in range(len(commands)):
		cmd = ' '.join([str(x) for x in commands[i]+args])
		if verbose: printDebug("run: %s" % cmd, "comment")
		if env:
			try:
				import subprocess
				return subprocess.check_output(cmd, shell=True, env=env)
			except Exception as e:
				printDebug(str(e), "error")
				return None
		else:
			import subprocess
			p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout,stderr = p.communicate()
			if not hide_stderr: print(stderr)
			if verbose: print(stdout)
			return stdout, p.returncode