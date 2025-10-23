def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	args = {}
	for unparsed_argument in unparsed_arguments:
		if unparsed_argument.startswith('--'):
			key, value = unparsed_argument[2:].split('=')
			args[key] = value
	return args