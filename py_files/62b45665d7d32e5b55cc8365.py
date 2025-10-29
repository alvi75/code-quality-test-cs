def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	args = {}
	for argument in unparsed_arguments:
		if '=' in argument:
			key, value = argument.split('=')
			args[key] = value
	return args