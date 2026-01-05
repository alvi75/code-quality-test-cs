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

	if not isinstance(extra_env, dict) or len(extra_env) == 0:
		extra_env = None

	try:
		return subprocess.run([func] + list(args), capture_output=True, text=True,
		                     env=extra_env, timeout=timeout)
	except subprocess.TimeoutExpired as e:
		raise TimeoutError("Timeout while running %s" % func) from e