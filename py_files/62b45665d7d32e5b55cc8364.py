def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).
	"""
	parsed_args = {}
	remaining_args = unparsed_arguments

	for subparser_name in sorted(subparsers.keys()):
		parser = subparsers[subparser_name]
		args = parser.parse_known_args(remaining_args)
		if args is None:
			continue
		else:
			parsed_args[subparser_name] = args
			remaining_args = args.args

	return parsed_args, remaining_args