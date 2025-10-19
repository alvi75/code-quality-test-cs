def _run_command(command, args, cwd, verbose, hide_stderr, env):
		if not isinstance(command, list):
			command = [command]
		subprocess.check_output([command[0]] + command[1:] + args, cwd=cwd, stderr=subprocess.STDOUT if hide_stderr else subprocess.PIPE, env=env)

		return subprocess.check_output([command[0]] + command[1:]), 0

	return _run_command