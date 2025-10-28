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
	if not isinstance(timeout, int):
		raise TypeError("timeout must be an integer")
	if not isinstance(extra_env, dict):
		raise TypeError("extra_env must be a dictionary")

	# Create a process object
	p = subprocess.Popen(args, env=extra_env)

	# Wait for the process to finish
	try:
		p.wait(timeout)
	except subprocess.TimeoutExpired:
		return None

	# Return the process object
	return p