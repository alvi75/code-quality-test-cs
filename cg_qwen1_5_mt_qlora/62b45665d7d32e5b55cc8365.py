def parse_arguments(*unparsed_arguments):
	"""
	Parses parameters and returns them as dict maps
	"""
	args = {}
	for arg in unparsed_arguments:
		if isinstance(arg, (list, tuple)):
			arg = arg[0]
		if not hasattr(arg, 'split'):
			continue
		key = arg.split('=')[0].strip()
		value = '='.join(arg.split('=')[1:]).strip()
		try:
			value = int(value)
		except ValueError:
			pass
		args[key] = value
	return args