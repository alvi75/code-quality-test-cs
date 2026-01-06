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

	if not hasattr(sys.modules[func.__module__], func.__name__):
		raise RuntimeError("Function %s does not exist" % func)

	func = sys.modules[func.__module__][func.__name__]

	return subprocess.run([sys.executable] + [func] + list(args), env=extra_env, timeout=timeout)