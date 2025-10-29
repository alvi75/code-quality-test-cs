def subprocess_run_helper(func, *args, timeout, extra_env=None):
	"""
	Run a function in a sub-process

    Args:
            func: function, the function to be run. It must be in a module that is importable.
            *args: str. Any additional command line arguments to be passed in
                        the first argument to ``subprocess.run``.
            extra_env: dict[str, str]. Any additional environment variables to be set for the subprocess.
    Returns:
            CompletedProcess instance
	"""
	if not isinstance(func, types.FunctionType):
		raise TypeError("func must be a function")
	if not isinstance(args, (list, tuple)):
		raise TypeError("args must be a list or tuple")
	if not isinstance(extra_env, dict):
		raise TypeError("extra_env must be a dictionary")

	# Create a process object
	process = subprocess.Popen(
			args,
			shell=not args[0].startswith("/bin/"),
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			creationflags=0,
			shell=False,
			env=extra_env,
		)

	# Wait for the process to finish
	try:
		output, error = process.communicate(timeout=timeout)
	except subprocess.TimeoutExpired:
		process.kill()
		output, error = process.communicate()

	# Return the output of the process
	return CompletedProcess(func, process.returncode, output, error)