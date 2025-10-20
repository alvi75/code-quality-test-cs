def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if isinstance(commands, six.string_types):
		commands = [commands]
	for cmd in commands:
		cmd = shlex.split(cmd)
		p = subprocess.Popen(
			cmd,
			cwd=cwd,
			stdout=subprocess.PIPE,
			stderr=subprocess.STDOUT if not hide_stderr else subprocess.DEVNULL,
			env=env or os.environ.copy(),
		)

		while True:
			line = p.stdout.readline()
			if line == b"":
				break

			if verbose:
				print(line.decode("utf-8"), end="")

		returncode = p.wait()

		if returncode != 0:
			raise RuntimeError("Command failed with exit code %d" % returncode)