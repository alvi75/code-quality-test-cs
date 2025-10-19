def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list):
		commands = [commands]
	for c in commands:
		if not os.path.exists(c):
			raise Exception("Command %s does not exist" % c)

	return_code = 0
	stdout = ""
	stderr = ""

	for cmd in commands:
		cmd = shlex.split(cmd)
		p = Popen(cmd, stdout=PIPE, stderr=PIPE, cwd=cwd, env=env, universal_newlines=True)
		out,err = p.communicate(input=args)
		if p.returncode != 0:
			if hide_stderr:
				pass
			else:
				sys.stderr.write(err.decode('utf-8'))
				sys.stderr.flush()
				raise Exception("Command %s failed: %s" % (cmd, err))
		stdout += out.decode('utf-8')
		return_code = p.returncode

	return stdout, return_code