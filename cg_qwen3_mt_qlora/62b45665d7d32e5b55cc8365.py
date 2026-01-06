def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	args = unparsed_arguments[0]
	if not args:
		return {}
	
	# Parse arguments
	parsed_args = {}
	for arg in args:
		key, value = arg.split('=')
		parsed_args[key] = value
	
	return parsed_args