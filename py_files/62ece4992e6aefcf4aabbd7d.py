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

	if extra_env is None:
		extra_env = {}

	# Get the current environment
	current_environ = os.environ.copy()

	# Set the environment variables
	for key, value in extra_env.items():
		current_environ[key] = value

	# Run the process
	try:
		return subprocess.run(
			func.__module__ + " " + ' '.join(args),
			shell=True,
			tty=False,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			banner=False,
			cwd=current_environ['PWD'],
			timeout=timeout,
			shell=True,
			environment=current_environ
		)
	except subprocess.TimeoutExpired as e:
		print(e.output)
		raise
	except Exception as e:
		print(e.output)
		raise