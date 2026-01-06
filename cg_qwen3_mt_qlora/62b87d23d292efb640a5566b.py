def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, (list, tuple)):
		commands = [commands]

	for cmd in commands:
		if verbose:
			print("Running: %s" % " ".join([cmd] + args))

		p = subprocess.Popen(
			cmd,
			cwd=cwd,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			env=env
		)

		out, err = p.communicate()

		if p.returncode != 0:
			raise Exception("Command failed with return code %d:\n%s\n%s" % (
				p.returncode,
				out.decode('utf-8'),
				err.decode('utf-8')
			))