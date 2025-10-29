def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list):
		commands = [commands]
	
	for cmd in commands:
		if verbose:
			print("Running: %s" % cmd)
		
		# Create the process
		process = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True, cwd=cwd, env=env)
		
		# Read the output
		stdout, stderr = process.communicate()
		
		# Decode the output
		if sys.version_info[0] >= 3:
			stdout = stdout.decode('utf-8')
			stderr = stderr.decode('utf-8')
		
		# Hide stderr if requested
		if hide_stderr:
			stderr = ""
		
		# Return the result
		return {
			'returncode': process.returncode,
			'stdout': stdout,
			'stderr': stderr
		}