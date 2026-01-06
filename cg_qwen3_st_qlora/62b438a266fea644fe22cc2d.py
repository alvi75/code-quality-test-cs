def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).
	"""
	parsed_arguments = {}
	remaining_arguments = []
	for subparser_name in subparsers:
		subparser = subparsers[subparser_name]
		try:
			namespace, remaining_arguments = subparser.parse_known_args(unparsed_arguments)
			parsed_arguments[subparser_name] = namespace
		except SystemExit:
			pass

	return parsed_arguments, remaining_arguments