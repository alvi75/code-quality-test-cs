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
    if not isinstance(func, types.FunctionType) or not hasattr(func, "__module__"):
        raise ValueError("func must be a function")
    try:
        module = __import__(func.__module__)
        return getattr(module, func.__name__)(*args, **extra_env)
    except (ImportError, AttributeError, TypeError) as e:
        raise RuntimeError("Failed to execute function %s" % func.__name__, e) from e