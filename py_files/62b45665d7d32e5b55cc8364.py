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
		# Find the subparser that can handle this argument.
		subparser = None
		for subparser_name, subparser in subparsers.items():
			if subparser.add_argument(argument) is not None:
				subparser = subparser
				break

		# If we found a subparser, try to parse it.
		if subparser is not None:
			namespace = subparser.parse_args([argument])
			parsed_arguments[subparser_name] = namespace
		else:
			# Otherwise, just add it to the remaining arguments.
			remaining_arguments.append(argument)

	return parsed_arguments, remaining_arguments