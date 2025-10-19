def xargs(
        cmd: tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs:
	"""
	Simplified Implementation of Xargs in Linux
	"""
	if not isinstance(cmd, tuple):
		raise TypeError("cmd must be a tuple")
	if not all(isinstance(x, str) for x in cmd):
		raise TypeError("cmd elements must be strings")
	if not isinstance(varargs, list):
		raise TypeError("varargs must be a list")
	if not all(isinstance(x, str) for x in varargs):
		raise TypeError("varargs elements must be strings")

	# TODO: Add support for more options

	# Prepare command
	cmd = [str(c) for c in cmd]
	args = []
	for arg in varargs:
		arg = str(arg)
		if len(arg) + len(args) + 1 > _max_length:
			args.append('"' + '" "'.join(args) + '"')
			args[:] = []
		args.append(arg)
	if args:
		args.append('" "'.join(args) + '"')

	# Execute command
	return shell.run(
		cmd=cmd + args,
		color=color,
		target_concurrency=target_concurrency,
		**kwargs
	)