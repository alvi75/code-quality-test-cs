def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, list):
		commands = [commands]

	for cmd in commands:
		if verbose:
			print("Running: %s" % (cmd,))
		try:
			subprocess.check_call([cmd] + args, cwd=cwd, env=env)
		except subprocess.CalledProcessError as e:
			if hide_stderr:
				print("Command failed with exit code %d" % (e.returncode,))
			else:
				print("Command failed with exit code %d\n%s" % (e.returncode, e.output))
			return False

	return True