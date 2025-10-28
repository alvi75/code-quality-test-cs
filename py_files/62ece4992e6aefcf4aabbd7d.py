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
		raise TypeError('extra_env should be a dictionary')

	try:
		import importlib.util
	except ImportError:
		# python 2.x
		import imp as importlib_util

		def import_module(name):
			return importlib_util.find_spec(name).loader.execfile(name)
	else:
		import importlib.util

		def import_module(name):
			return importlib.util.spec_from_file_location(name, name).__class__.from_loader(
				importlib.util.spec_from_file_location(name, name), None)

	mod = import_module(func.__module__)
	func = getattr(mod, func.__name__)

	args = [sys.executable] + list(args) + ['--'] + sys.argv[1:]
	cmd = ' '.join(args)
	logger.debug("Running %s", cmd)

	env = os.environ.copy()
	for k, v in extra_env.items():
		env[k] = v

	result = subprocess.run(args,
	                        stdout=subprocess.PIPE,
	                        stderr=subprocess.STDOUT,
	                        env=env,
	                        timeout=timeout,
	                        check=True)
	return result