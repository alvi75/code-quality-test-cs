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
    # Get the module that the function is in
    module = func.__module__
    # Get the function name
    func_name = func.__name__
    # Get the full path to the module
    module_path = os.path.abspath(module.__file__)
    # Get the full path to the function
    func_path = os.path.join(module_path, func_name)
    # Get the full path to the function
    func_path = os.path.abspath(func_path)
    # Get the full path to the function
    func_path = os.path.realpath(func_path)
    # Get the full path to the function
    func_path = os.path.normpath(func_path)
    # Get the full path to the function
    func_path = os.path.expanduser(func_path)
    # Get the full path to the function
    func_path = os.path.expandvars(func_path)
    # Get the full path to the function
    func_path = os.path.expandvars(func_path)
    # Get the full path to the function
    func_path = os.path.expandvars(func_path)
    # Get the full path to the function
    func_path = os.path.expandvars(func_path)
    # Get the full path to the function
    func_path = os.path.expandvars(func_path)
    # Get the full path to the function
    func_path = os.path.expandvars(func_path)