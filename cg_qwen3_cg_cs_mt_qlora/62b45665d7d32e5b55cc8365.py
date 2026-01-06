def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	args = {}
	for unparsed_argument in unparsed_arguments:
		if "=" in unparsed_argument:
			key, value = unparsed_argument.split("=", 1)
			args[key] = value
	return args