def parse_subparser_arguments(unparsed_arguments, subparsers):
	"""
	Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
instance, give each requested action's subparser a shot at parsing all arguments. This allows
common arguments like "--repository" to be shared across multiple subparsers.

Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
arguments, a list of remaining arguments not claimed by any subparser).
	"""
	namespaces = {}
	remaining_arguments = []
	while unparsed_arguments:
		argument = unparsed_arguments[0]
		unparsed_arguments = unparsed_arguments[1:]

		if argument in subparsers:
			subparser = subparsers[argument]
			try:
				namespace, unparsed_tail = subparser.parse_known_args(unparsed_arguments)
				namespaces[argument] = namespace
				remaining_arguments.extend(unparsed_tail)
				break
			except SystemExit:
				pass

		# No match; keep this argument for later.
		remaining_arguments.append(argument)

	return namespaces, remaining_arguments