def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	A list of command is given. Run the given command(s) with the given arguments use a subprocess. Return the running result (stdout and returncode)
	"""
	if not isinstance(commands, list):
		raise TypeError("commands must be a list")
	for c in commands:
		if not isinstance(c, str):
			raise TypeError("each element in commands must be a string")

	if not isinstance(args, list):
		args = [args]

	if not isinstance(env, dict):
		env = {}

	result = None

	try:
		process = subprocess.Popen(
			[os.path.join(os.getcwd(), c)] + args,
			cwd=cwd,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE if hide_stderr else subprocess.PIPE,
			env=env)

		output, error = process.communicate()
		return_code = process.returncode

		if verbose:
			print(output.decode('utf-8'))
			print(error.decode('utf-8'))

		result = {
			"output": output.decode('utf-8'),
			"error": error.decode('utf-8') if not hide_stderr else "",
			"return_code": return_code
		}

	except Exception as e:
		result = {
			"output": "",
			"error": str(e),
			"return_code": -1
		}
	
	return result