def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
	"""
	Call the given command(s).
	"""
	if not isinstance(commands, list):
		commands = [commands]
	if not isinstance(args, list):
		args = [args]

	cmds = []
	for cmd in commands:
		if isinstance(cmd, str):
			cmd = shlex.split(cmd)
		elif isinstance(cmd, list):
			pass
		else:
			raise ValueError("Commands must be strings or lists of strings")

		if len(cmd) == 0:
			continue

		if len(cmd) > 1 and cmd[0] == 'cd':
			cwd = cmd[1]
			cmd = cmd[2:]

		if len(cmd) > 1 and cmd[0] == 'env':
			env = cmd[1:]
			cmd = cmd[2:]

		if len(cmd) > 1 and cmd[0] == 'hide':
			hide_stderr = True
			cmd = cmd[1:]

		if len(cmd) > 1 and cmd[0] == 'verbose':
			verbose = True
			cmd = cmd[1:]

		if len(cmd) > 1 and cmd[0] == 'cwd':
			cwd = cmd[1:]
			cmd = cmd[2:]

		if len(cmd) > 1 and cmd[0] == 'env':
			env = cmd[1:]
			cmd = cmd[2:]

		if len(cmd) > 1 and cmd[0] == 'hide':
			hide_stderr = True
			cmd = cmd[1:]

		if len(cmd) > 1 and cmd[0] == 'verbose':
			verbose = True
			cmd = cmd[1:]

		if len(cmd) > 1 and cmd[0] == 'cwd':
			cwd = cmd[1:]
			cmd = cmd[2:]

		if len(cmd) > 1 and cmd[0] == 'env':
			env = cmd[1:]
			cmd = cmd[2:]

		if len(cmd) > 1 and cmd[0] == 'hide':
			hide_stderr = True
			cmd = cmd[1:]

		if len(cmd) > 1 and cmd[0] == 'verbose':
			verbose = True
			cmd = cmd[1:]

		if len(cmd) > 1 and cmd[0] == 'cwd':
			cwd