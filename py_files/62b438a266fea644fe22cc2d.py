def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).
	"""
	parsed = {}
	remaining = []
	for subparser in subparsers.values():
		subparser_args, remaining = subparser.parse_known_args(unparsed_arguments)
		if subparser_args.action:
			parsed[subparser_args.action] = subparser_args

	return parsed, remaining