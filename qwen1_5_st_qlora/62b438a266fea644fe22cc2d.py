def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
	instance, give each requested action's subparser a shot at parsing all arguments. This allows
	common arguments like "--repository" to be shared across multiple subparsers.

	Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
	arguments, a list of remaining arguments not claimed by any subparser).
	"""

	parsed_args = {}
	unclaimed_args = []
	for subparser_name in sorted(subparsers.keys()):
		subparser = subparsers[subparser_name]
		try:
			args = subparser.parse_known_args(unparsed_arguments)
			if args is None or len(args) == 0:
				raise ValueError("Subparser %s returned no arguments." % subparser_name)

			parsed_args[subparser_name] = args[0]
			unclaimed_args.extend(args[1:])
		except SystemExit:
			pass

	return parsed_args, unclaimed_args