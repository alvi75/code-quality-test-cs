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
	if not isinstance(varargs, (list, tuple)):
		varargs = [varargs]
	cmd = list(cmd)
	for i, arg in enumerate(varargs):
		if len(arg) > _max_length:
			raise ValueError(f"Argument {i} is too long")
		cmd.append(arg)

	return subprocess.Popen(
		cmd,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		close_fds=True,
		universal_newlines=True,
		preexec_fn=os.setsid,
		factory=ProcessFactory(target_concurrency=target_concurrency),
		color=color,
		**kwargs
	)