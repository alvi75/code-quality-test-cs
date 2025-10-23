def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).
	"""
	subparser_names = set(subparsers.keys())
	parsed_arguments = {}
	remaining_arguments = []
	for argument in unparsed_arguments:
		if argument in subparser_names:
			subparser_name = argument
			subparser = subparsers[subparser_name]
			subparser_arguments = subparser.parse_args([argument] + unparsed_arguments)
			parsed_arguments[subparser_name] = subparser_arguments
			remaining_arguments = unparsed_arguments[len(argument) + 1:]
		else:
			remaining_arguments.append(argument)

	return parsed_arguments, remaining_arguments