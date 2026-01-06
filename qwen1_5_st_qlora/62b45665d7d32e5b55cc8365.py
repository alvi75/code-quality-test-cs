def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	args = {}
	for arg in unparsed_arguments:
		if '=' not in arg:
			raise ValueError("Invalid argument: %s" % arg)
		key, value = arg.split('=', 1)
		try:
			value = int(value)
		except ValueError:
			pass
		args[key] = value
	return args