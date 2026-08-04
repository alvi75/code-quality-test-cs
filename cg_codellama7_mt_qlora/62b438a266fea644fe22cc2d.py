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
	for argument in unparsed_arguments:
		for subparser_name, subparser in subparsers.items():
			try:
				parsed_arguments[subparser_name] = subparser.parse_args([argument])
			except SystemExit:
				pass
			else:
				break
		else:
			remaining_arguments.append(argument)
	return parsed_arguments, remaining_arguments