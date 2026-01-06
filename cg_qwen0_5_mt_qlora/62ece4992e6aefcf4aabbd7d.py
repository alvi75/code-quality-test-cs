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

	# Get the full path of the executable
	exe = os.path.abspath(os.path.join(os.path.dirname(__file__), func.__module__))

	# Create the command line arguments
	cmd = [exe] + list(args)

	# Set up the environment
	env = os.environ.copy()
	env.update(extra_env)

	# Set up the timeout
	timeout = timeout

	# Run the process
	try:
		return subprocess.run(cmd,
			cwd=os.getcwd(),
			shell=False,
			check=True,
			creationflags=0o755 | 0o644,
			environment=env,
			timeout=timeout)
	except subprocess.CalledProcessError as e:
		return CompletedProcess(e.returncode, cmd, output=e.output)