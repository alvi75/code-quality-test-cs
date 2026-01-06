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
	if not isinstance(extra_env, dict):
		raise TypeError("extra_env must be a dictionary")
	if not isinstance(timeout, int):
		raise TypeError("timeout must be an integer")

	# Get the path of the executable
	exe_path = os.path.dirname(os.path.abspath(__file__))
	exe_path = exe_path + "/"

	# Create the command string
	cmd = [exe_path + func] + list(args)

	# Set up the environment
	env = os.environ.copy()
	env.update(extra_env)
	env['PYTHONPATH'] = exe_path

	# Run the process
	try:
		return subprocess.run(cmd, env=env, timeout=timeout, check=True)
	except subprocess.TimeoutExpired:
		return subprocess.run(cmd, env=env, timeout=timeout, check=False)