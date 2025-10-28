def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	args = {}
	for arg in unparsed_arguments:
		if isinstance(arg, basestring) or not hasattr(arg, '__iter__'):
			arg = [arg]
		for a in arg:
			try:
				key, value = a.split('=', 1)
			except ValueError:
				raise ValueError("Invalid argument: %s" % a)
			args[key] = value
	return args