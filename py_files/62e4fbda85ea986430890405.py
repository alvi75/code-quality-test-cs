def xargs(
		cmd: tuple[str, ...],
		varargs: Sequence[str],
		*,
		color: bool = False,
		target_concurrency: int = 1,
		_max_length: int = _get_platform_max_length(),
		**kwargs:
	) -> None:
	"""
	Simplified Implementation of Xargs in Linux
	"""
	if not isinstance(cmd, list):
		raise TypeError("cmd must be a list")
	if not isinstance(varargs, list):
		raise TypeError("varargs must be a list")

	# Get the length of each argument
	lengths = [len(x) for x in varargs]

	# Sort the lengths
	lengths.sort(reverse=True)

	# Get the max length
	max_length = _max_length

	# Get the number of arguments to pass to the command
	num_args = len(cmd)
	num_args -= len([x for x in varargs if x is not None])

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to pass to the command
	num_args //= num_args % 2

	# Get the number of arguments to